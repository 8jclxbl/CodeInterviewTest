def NumberOf1(n):
        # write code here
        count = 0
        while n :
            if n % 2 == 1: 
                count += 1
            print(n)
            n = n >> 1
        return count

def NumberOf1_best(n):
        # write code here
        return sum([(n>>i & 1) for i in range(0,32)])

def NumberOf1_me(n):
    return bin(n & 0xffffffff).count('1') 