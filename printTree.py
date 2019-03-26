from myTree import Tree,TreeNode

test = Tree([8,7,6,3,4,5,6])

def printTree(pRoot):
    if not pRoot:return []
    res = [[pRoot.val]]
    queue = [pRoot]
    epoch = 1
    while True:
        temp = []
        printTemp = []
        count = 0
        while queue:
            current = queue.pop(0)
            if not current:
                continue
            else:
                if current.left:
                    temp.append(current.left)
                    printTemp.append(current.left.val)
                    count += 1
                if current.right:
                    temp.append(current.right)
                    printTemp.append(current.right.val)
                    count += 1

        if count == 0: break
        if epoch%2 == 1:printTemp = printTemp[::-1]
        res.append(printTemp)
        queue = temp
        epoch += 1
    return res

print(printTree(test.Root))