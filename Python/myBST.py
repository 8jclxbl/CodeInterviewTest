#若树中已存在了要插入的结点
class DupValueError(Exception):
    def __init__(self,val):
        self.message = 'The node has inserted in the BST, the Value is' + str(val)
        #print(self.message)
#若树中不存在要删除的结点
class NoSuchNodeError(Exception):
    def __init__(self,val):
        self.message = 'The node has not found in the BST, the Value is' + str(val)
        #print(self.message)

#结点类
class TreeNode:
    def __init__(self, val):
        self.val = val
        #结点类型，根，左子，右子
        self.nodeType = 'root'

        self.left = None
        self.right = None
        #父节点
        self.parent = None
        #此节点在书中的高度
        self.height = 0

    #结点是否是叶结点
    def isLeaf(self):
        if self.hasLeft() or self.hasRight():return False
        else: return True

    #检测是否存在左右子树
    def hasLeft(self):
        return self.left is not None
    def hasRight(self):
        return self.right is not None


class Bst:
    def __init__(self):
        self.root = None
        self.treeHeight = self.height(self.root)

    def getMax(self,root):
        if not root: return None
        if root.right:
            return self.getMax(root.right)
        else:
            return root

    def getMin(self,root):
        if not root: return None
        if root.left:
            return self.getMin(root.left)
        else:
            return root

    #结算结点高度
    def height(self,root):
        if not root:
            return 0
        else:
            root.height = 1 + max(self.height(root.left), self.height(root.right))
            return root.height

    def priorTravers(self,root):
        if root:
            print(root.val)
            self.priorTravers(root.left)
            self.priorTravers(root.right)

    #更新结点高度
    """
    def updateHeight(self,root):
        if not root: return None
        else:
            root.height = self.height(root)
            self.updateHeight(root.left)
            self.updateHeight(root.right)
    """
    def genFromList(self,nodeList):
        self.root = TreeNode(nodeList[0])
        for i in nodeList[1:]:
            self.insert(i)
        self.height = self.root.height
        return self.root

    #给结点添加左子树
    def addAsLeft(self,parent,child):
        if child:
            parent.left = child
            child.nodeType = 'left'
            child.parent = parent
        else:
            parent.left = None

    def addAsRight(self,parent,child):
        if child:
            parent.right = child
            child.nodeType = 'right'
            child.parent = parent
        else:
            parent.right = None
    def removeLeft(self,parent):
        parent.left.parent = None
        parent.left = None

    def removeRight(self,parent):
        parent.right.parent = None
        parent.right = None

    def removeLeaf(self,node):
        if node.nodeType == 'left':
            self.removeLeft(node.parent)
        else:
            self.removeRight(node.parent)

    def removeRoot(self,node):
        p = node.parent
        if not node.right:
            if node.nodeType == 'left':
                self.removeLeft(p)
                self.addAsLeft(p,node.left)
            else:
                self.removeRight(p)
                self.addAsRight(p,node.left)
        else:
            min_ = node.right
            if not node.right.hasLeft():
                min_.left = node.left
                if node.nodeType == 'left':
                    self.removeLeft(p)
                    self.addAsLeft(p,min_)
                elif node.nodeType == 'right':
                    self.removeRight(p)
                    self.addAsRight(p,min_)
                else:
                    self.root = min_
                self.addAsLeft(min_,node.left)
            else:
                while min_.left:
                    min_ = min_.left

                self.removeLeft(min_.parent)
                if node.nodeType == 'left':
                    self.removeLeft(p)
                    self.addAsLeft(p,min_)
                elif node.nodeType == 'right':
                    self.removeRight(p)
                    self.addAsRight(p,min_)
                else:
                    self.root = min_
                self.addAsLeft(min_,node.left)
                self.addAsRight(min_,node.right)

    #实际的递归搜索函数
    def _search(self,root,key):
        if root.val > key:
            if not root.left:
                return root
            else:  
                return self._search(root.left,key)
        elif root.val < key:
            if not root.right:
                return root
            else:
                return self._search(root.right,key)
        else:
            return root

    #在树中搜索key指定的结点
    def search(self,root,key):
        if not root: return None
        else:
            return self._search(root,key)

    #这里插入的输入时结点的值，函数中会根据值建立结点
    def insert(self, val):
        cur = self.search(self.root,val)
        if cur.val == val: 
            raise DupValueError(val)
        newNode = TreeNode(val)
        if cur.val > val:
            self.addAsLeft(cur,newNode)
        else:
            self.addAsRight(cur,newNode)

        self.height(self.root)
        return newNode

    def delete(self,val):
        cur = self.search(self.root,val)
        p = cur.parent
        if cur.val != val:
            raise NoSuchNodeError(val)
        else:
            if cur.isLeaf():
                self.removeLeaf(cur)
            else:
                self.removeRoot(cur)

            if not p:return self.root
            return p


"""test = [10,30,65,50,90,40]
bst = Bst()
bst.genFromList(test)
#bst.priorTravers(bst.root)
#bst.delete(8)
bst.priorTravers(bst.root)
print(bst.root.height)

"""