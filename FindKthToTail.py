def FindKthToTail(head, k):
        # write code here
        fast = slow = head
        i = 0
        if i >= k:return None
        while i < k-1:
            if fast and fast.next:
                fast = fast.next
            else:return None
            i += 1
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow

def FindKthToTail_me(head, k):
        # write code here
        if k <= 0: return None
        temp = []
        count = 0
        while head:
            temp.append(head)
            if count < k:
                count += 1
            else:
                temp.pop(0)
            head = head.next
        if count < k:return None
        return temp[0]
