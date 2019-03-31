class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, values):
        self.numNodes = len(values)
        self.Nodes = []
        self.genTreeFromList(values)
        self.Root = self.Nodes[0]
    
    def genTreeFromList(self,values):
        for i in range(self.numNodes):
            if values[i] == '#':
                self.Nodes.append(None)
            self.Nodes.append(TreeNode(values[i]))
        
        for i in range(self.numNodes):
            if not self.Nodes[i]:
                continue
            if i*2 + 1 < self.numNodes:self.Nodes[i].left = self.Nodes[i*2 + 1]
            if i*2 + 2 < self.numNodes:self.Nodes[i].right = self.Nodes[i*2 + 2]

    def prior_traverse(self,Root):
        if Root:
            print(Root.val)
            self.prior_traverse(Root.left)
            self.prior_traverse(Root.right)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class List:
    def __init__(self, values):
        if not isinstance(values,list) or len(values) == 0:
            self.root = None
            self.cur = self.root
            self.size = 0
        else:
            self.root = ListNode(values[0])
            self.cur = self.root
            self.size = 1
            self.addList(values[1:])
        
    def add(self,val):
        self.cur.next = ListNode(val)
        self.cur = self.cur.next
        self.size += 1
        
    def addList(self, values):
        for i in values:
            self.add(i)

    def traverse(self):
        count = 0
        root = self.root
        while root and count < self.size:
            print(root.val)
            root = root.next
            count += 1
    
