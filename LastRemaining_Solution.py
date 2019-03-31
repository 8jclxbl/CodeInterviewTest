from myds import List

def LastRemaining_Solution(n, m):
    children = List(list(range(n)))
    children.cur.next = children.root
    ptr = children.root
    while children.size > 1:
        for i in range(m-2):
            ptr = ptr.next
        ptr.next = ptr.next.next
        ptr = ptr.next
        children.size -= 1
    
    return ptr.val
for i in range(1,10):
    print(LastRemaining_Solution(4,i))