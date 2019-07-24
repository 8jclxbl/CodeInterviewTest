def PrintFromTopToBottom(root):
        # write code here
        if not root: return None
        total = [[root]]
        last_length = 1
        while True:
            length = 0
            temp = []
            count = 0
            for i in total[-1]:
                if i == '#':continue
                if i.left:
                    temp.append(i.left)
                    length += 1
                else:
                    temp.append('#')
                    count += 1
                if i.right:
                    temp.append(i.right)
                    length += 1
                else:
                    temp.append('#')
                    count += 1
            if count == last_length * 2:
                result = []
                for i in total:
                    i_val = [j.val for j in i if j != '#']
                    result += i_val
                return result
            last_length = length
            total.append(temp)

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
root.left = a
root.right = b
print(PrintFromTopToBottom(root))