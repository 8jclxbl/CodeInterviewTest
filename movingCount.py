class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.r = rows
        self.c = cols
        self.threshold = threshold
        self.mask = [0 for i in range(rows * cols)]
        return self._search(0,0)

    def _search(self,x,y):
        temp = x * self.c + y
        if x >= self.r or y >= self.c or x < 0 or y < 0 or self._compute(x,y) or self.mask[temp]:
            return 0
        self.mask[temp] = 1
        return 1 + self._search(x + 1,y) + self._search(x - 1,y) + self._search(x,y + 1) + self._search(x,y - 1)
        
    def _compute(self,x,y):
        x = str(x)
        y = str(y)
        sum = 0
        for i in x+y:
            sum += int(i)
        
        return sum > self.threshold
        

s = Solution()
print(s.movingCount(10,5,5))
print(s.mask)