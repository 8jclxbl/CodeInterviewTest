class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5: return False
        count0 = 0
        max_ = 0
        min_ = 14
        dic = {}
        for i in numbers:
            if i == 0:
                count0 += 1
            else:
                if i in dic: return  False
                else: dic[i] = 1
            if i > max_: max_ = i
            if i < min_ and i != 0: min_ = i

        if count0 == 4: return True
        if max_ - min_  <= 4: return True 
        else:return False
        
s = Solution()
a = [i for i in range(0,14)] * 4
print([1,3,2,4,6], s.IsContinuous([1,3,2,4,6]))
print(a)
import random
for i in range(10):
    b = random.sample(range(0,54),5)
    c = [a[i] for i in b]
    print(c, s.IsContinuous(c))