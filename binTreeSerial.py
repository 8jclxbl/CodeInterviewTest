from myTree import TreeNode
def Serialize(root):
    if not root:return '#'
    else: 
        return '{0},{1},{2}'.format(root.val,Serialize(root.left),Serialize(root.right))

def prior_traverse(Root):
        if Root:
            print(Root.val)
            prior_traverse(Root.left)
            prior_traverse(Root.right)


idx = -1
def Deserialize(s):
    # write code here
    return deserialize(s)
    
def deserialize(s):
    global idx
    idx += 1
    if idx >= len(s):
        return None
    if s[idx] == '#':return None
    else:
        root = TreeNode(int(s[idx]))
        root.left = deserialize(s)
        root.right = deserialize(s)
        return root


root = Deserialize([5,4,'#',3,'#',2])
prior_traverse(root)
print(Serialize(root))