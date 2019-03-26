class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
def traverse(node):
    while node:
        print(node.val)
        node = node.next

def deleteDuplication(pHead):
        # write code here
        pre = ListNode(0)
        pre = pHead
        nxt = pHead.next
        ctn = False
        while nxt:
            if nxt.val == pHead.val:
                print(nxt.val,pHead.val)
                ctn = True
            else:
                
                pHead.next = nxt
                ctn = False
                pHead = nxt
            nxt = nxt.next
        if ctn: pHead.next.next = None
        return pre

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(4)
g = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

print(traverse(deleteDuplication(a)))