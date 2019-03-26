def Mirror(self, root):
        # write code here
        if root:
            root.left,root.right = root.right,root.left
            self.Mirror(root.left)
            self.Mirror(root.right)