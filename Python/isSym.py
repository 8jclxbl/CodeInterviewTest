from myds import Tree
class Solution:
    def isSymmetrical(self,pRoot):
        # write code here
        if not pRoot:
            return True
        else:
            return self.isSame(pRoot.left,pRoot.right)
        
    def isSame(self,root1,root2):
        if not root1 and not root2:
            return True 
        if root1 and root2 and root1.val == root2.val:
            return (self.isSame(root1.left,root2.right)) and (self.isSame(root1.right,root2.left))
        
        return False
            

t1 = Tree([8,6,9,6,5,5,6])
#t2 = Tree([8,7,7,6,5,5,6])
print(isSymmetrical(t1.Root))
#print(isSymmetrical(t2.Root))