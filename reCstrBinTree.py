from myds import TreeNode
def reConstructBinaryTree(pre, tin): 
    if len(pre) == 0:return None
    cur = pre[0]
    idx = tin.index(cur)
    t_left = tin[:idx]
    t_right = tin[idx + 1:]
    l_len = len(t_left)
    p_left = pre[1:l_len+1]
    p_right = pre[l_len+1:]

    root = TreeNode(cur)
    root.left = reConstructBinaryTree(p_left, t_left)
    root.right = reConstructBinaryTree(p_right, t_right)
    return root

def preTr(root):
    if root:
        print(root.val)
        preTr(root.left)
        preTr(root.right)

temp = reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
preTr(temp)

