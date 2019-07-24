from myBST import Bst,TreeNode,DupValueError,NoSuchNodeError

class AvlNode(TreeNode):
    def __init__(self, val):
        super().__init__(val)
        #平衡因子
        self.fc = 0

class AVL(Bst):
    def __init__(self):
        super().__init__()

    def genFromList(self,nodeList):
        self.root = AvlNode(nodeList[0])
        for i in nodeList[1:]:
            self.insert(i)
        self.height = self.root.height
        return self.root

    #找到更高的子树，用于平衡调整
    def tallerChild(self,root):
        if not root or root.isLeaf():return None
        if not root.left:
            l = 0
        else:
            l = root.left.height

        if not root.right:
            r = 0
        else:
            r = root.right.height
        if l >= r:return root.left
        else:return root.right

    #计算平衡因子
    def computeFc(self,root):
        if root.isLeaf():return 0
        if not root.left:
            l = 0
        else:
            l = root.left.height

        if not root.right:
            r = 0
        else:
            r = root.right.height
        root.fc = l-r
        return root.fc

    #平衡因子绝对值大于1表示不平衡
    def notBalance(self,root):
        if abs(self.computeFc(root)) > 1:return True
        else: return False

    #插入节点
    #由于插入结点中 结点的属性发生了变化，所以不能直接用super().insert
    #todo 将按值插入改为按结点插入，就可以这样写
        #以后有空重构一波
    def insert(self,val):
        cur = self.search(self.root,val)
        if cur.val == val: 
            raise DupValueError(val)
        newNode = AvlNode(val)
        if cur.val > val:
            self.addAsLeft(cur,newNode)
        else:
            self.addAsRight(cur,newNode)
        #添加完成后更新树的高度
        self.height(self.root)

        #看新插入结点的父节点是否平衡
        node = newNode.parent
        while node:
            if self.notBalance(node):
                #TO DO: adjust
                self.adjust(node)
                break
            node = node.parent

    def delete(self,val):
        node = super().delete(val)
        node = node.parent
        while node:
            if self.notBalance(node):
                #TO DO: adjust
                
                self.adjust(node)
            node = node.parent
        
    def adjust(self,root):
        g = root
        p = self.tallerChild(g)
        v = self.tallerChild(p)

        if p.nodeType == 'left':
            if v.nodeType == 'left':
                self.connect34(g, v,p,g, v.left,v.right,p.right,g.right)
            else:
                self.connect34(g, p,v,g, p.left,v.left,v.right,g.right)
        else:
            if v.nodeType == 'left':
                self.connect34(g, g,v,p, g.left,v.left,v.right,p.right)
            else:
                self.connect34(g, g,p,v, g.left,p.left,v.left,v.right)

    def connect34(self,g,a,b,c,t1,t2,t3,t4):
        if not g.parent:
            self.root = b
            b.nodeType = 'root'
            b.parent = None
        else:
            if g.nodeType == 'left':
                self.addAsLeft(g.parent,b)
            else:
                self.addAsRight(g.parent,b)

        self.addAsLeft(a,t1)
        self.addAsRight(a,t2)

        self.addAsLeft(c,t3)
        self.addAsRight(c,t4)

        self.addAsLeft(b,a)
        self.addAsRight(b,c)
        self.height(self.root)


test = [10,30,65,50,90,40]
avl = AVL()
avl.genFromList(test)
avl.priorTravers(avl.root)
print(avl.root.height)