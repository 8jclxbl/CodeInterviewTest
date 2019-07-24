# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    def __str__(self):
        rand = []
        value = []
        while self:
            if self.random:
                rand.append(str(self.random.label))
            else:
                rand.append('#')

            if self:
                value.append(str(self.label))
            else:
                rand.append('#')
            #value.append(str(self.label))
            self = self.next
        return ''.join(value +['|'] + rand)

a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
d = RandomListNode(4)
e = RandomListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

a.random = c
b.random = e
d.random = b


def Clone(pHead):
    # write code here
    start = pHead
    while pHead:
        temp = RandomListNode(pHead.label)
        pHead.next,temp.next = temp,pHead.next
        pHead = pHead.next.next
    pHead = start
    
    while pHead:
        if pHead.random:
            pHead.next.random = pHead.random.next
        pHead = pHead.next.next
    pHead = start
    copy = pHead.next
    
    while pHead:
        nxt = pHead.next.next
        if not nxt:break
        pHead.next.next = nxt.next
        pHead.next = nxt
        pHead = nxt
    pHead.next = None
    return copy
print(Clone(a))
print(a)