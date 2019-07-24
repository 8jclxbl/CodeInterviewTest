def Add(num1, num2):
    sum_list = []
    carry = 0
    while True:
        if not num1 and not num2:
            if carry:sum_list.insert(0,'1')
            break
        if not num1: a1 = 0
        else: a1 = num1 & 1
        if not num2: a2 = 0
        else: a2 = num2 & 1

        num1 = num1 >> 1
        num2 = num2 >> 1
        
        if a1 & a2:
            if carry: 
                sum_list.insert(0,'1')
            else:
                sum_list.insert(0,'0')
                carry = 1
            continue
        
        if a1 | a2:
            if carry:
                sum_list.insert(0,'0')
                carry = 1
            else:
                sum_list.insert(0,'1')
            continue

        if carry:
            sum_list.insert(0,'1')
            carry = 0
        else:
            sum_list.insert(0,'0')
    
    print(sum_list)
    res = ''.join(sum_list)
    return int(res,2)

def best_Add(self, num1, num2):
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        while num2 != 0:
            num1, num2 = (num1 ^ num2), ((num1 & num2) << 1)
            num1 = num1 & mask
            num2 = num2 & mask
        return num1 if num1 <= MAX else ~(num1 ^ mask)

print(Add(1,1))


        
                