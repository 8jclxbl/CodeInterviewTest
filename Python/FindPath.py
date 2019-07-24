from myds import TreeNode

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(3)
g = TreeNode(3)
h = TreeNode(2)
i = TreeNode(2)
j = TreeNode(1)
k = TreeNode(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h
d.right = i
e.left = j
e.right = k

def FindPath(root, expectNumber):
            # write code here
            
        if not root: return []
        expectNumber = expectNumber - root.val
        if expectNumber < 0:return []
        elif not root.left and not root.right and expectNumber == 0:return [[root.val]]
        else:
            res = []
            templ, tempr = FindPath(root.left,expectNumber),FindPath(root.right,expectNumber)
            for i in templ+tempr:
                res.append([root.val]+i)
            return res


print(FindPath(a,9))
