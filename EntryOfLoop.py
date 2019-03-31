from myds import ListNode,List
test = List([1,2,3,4,5,6])
test.cur.next = test.root.next.next

def EntryOfLoop(pHead):
    fast = slow = pHead
    while True:
        if slow:
            slow = slow.next
        else:return None
        if fast and fast.next:
            fast = fast.next.next
        else:return None
        if fast == slow:break
    
    fast = pHead
    while True:
        if fast == slow:return fast
        else:
            fast = fast.next
            slow = slow.next

print(EntryOfLoop(test.root).val)