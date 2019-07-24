from myds import Tree,TreeNode

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        #print(pRoot.val,k)
        if not pRoot:return None
        if self.num_nodes(pRoot) < k:return None
        temp = self.num_nodes(pRoot.left)
        if temp == k-1: return pRoot
        if temp > k:
            return self.KthNode(pRoot.left,k)
        elif temp == k:
            cur = pRoot.left
            while cur.right:
                cur = cur.right
            return cur
        else:
            return self.KthNode(pRoot.right,k-temp-1)
             
    def num_nodes(self, root):
        if root:
            return 1 + self.num_nodes(root.left) + self.num_nodes(root.right)
        else:
            return 0

test = Tree([8,6,10,5,7,9,11])
s = Solution()
#print(s.num_nodes(test.Root))
for i in range(1,8):
    print(s.KthNode(test.Root,i).val)