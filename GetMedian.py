class Solution:
    def __init__(self):
        self.data = []
        self.length = 0
    def Insert(self, num):
        # write code here
        if not self.length: 
            self.data.append(num)
        else:
            i = 0
            while i < self.length:
                if self.data[i] <= num:
                    i += 1
                else:
                    break
            self.data.insert(i,num)
        self.length += 1
    def GetMedian(self):
        # write code here
        if self.length%2 == 1: return self.data[self.length//2]
        else: return (self.data[self.length//2-1] + self.data[self.length//2])/2.0


s = Solution()
test = [5,2,3,4,1,6,7,0,8]
for i in test:
    s.Insert(i)
    print(s.data)
    print(s.GetMedian())