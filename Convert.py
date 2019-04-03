from myAVL import AVL

class Solution_B:
    def Convert(self,pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left
 
        # 连接根与左子树最大结点
        if left:
            while(left.right):
                left=left.right
            pRootOfTree.left,left.right=left,pRootOfTree
 
        # 处理右子树
        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right
 
        # 连接根与右子树最小结点
        if right:
            while(right.left):
                right=right.left
            pRootOfTree.right,right.left=right,pRootOfTree
             
        while(pRootOfTree.left):
            pRootOfTree=pRootOfTree.left
        return pRootOfTree


class Solution:
    def isLeaf(self,root):
        if not root.left and not root.right:
            return True
        else: 
            return False

    def pl(self, pRootOfTree):  
        pRootOfTree.left = self.Convert(pRootOfTree.left)
        if pRootOfTree.left != None:
            pRootOfTree.left.right = pRootOfTree
        if pRootOfTree.right:
            if self.isLeaf(pRootOfTree.right):
                pRootOfTree.right.left = pRootOfTree
                return pRootOfTree.right
            else:
                pRootOfTree.right = self.Convert(pRootOfTree.right)
                if pRootOfTree.right != None:
                    pRootOfTree.right.left = pRootOfTree
                return pRootOfTree 

    def pr(self, pRootOfTree):
        pRootOfTree.right = self.Convert(pRootOfTree.right)
        if pRootOfTree.right != None:
            pRootOfTree.right.left = pRootOfTree
        if pRootOfTree.left:
            if self.isLeaf(pRootOfTree.left):
                pRootOfTree.left.right = pRootOfTree
                return pRootOfTree.left
            else:
                pRootOfTree.left = self.Convert(pRootOfTree.left)
                if pRootOfTree.left != None:
                    pRootOfTree.left.right = pRootOfTree
                return pRootOfTree

    def Convert(self, pRootOfTree):
        if pRootOfTree.left:
            pRootOfTree.left = self.pl(pRootOfTree.left)
            pRootOfTree.left.right = pRootOfTree
        if pRootOfTree.right:
            pRootOfTree.right = self.pr(pRootOfTree.right)
            pRootOfTree.right.left = pRootOfTree
        else:
            return pRootOfTree
                

b = AVL()
b.genFromList([1,2,3,4,5,6,7])
s = Solution()
b.priorTravers(b.root)
en = b.getMax(b.root)
st = b.getMin(b.root)
s.Convert(b.root) 

cur = st
temp1 = []
while cur:
    if cur in temp1:
        break
    else:
        temp1.append(cur)
        cur = cur.right

cur = en
temp2 = []
while cur:
    if cur in temp2:
        break
    else:
        temp2.append(cur)
        cur = cur.left
print([i.val for i in temp1])
print([i.val for i in temp2])
