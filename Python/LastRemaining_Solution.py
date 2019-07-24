class Solution:
    def LastRemaining_Solution_r(self, n, m):
        if n == 0:return None
        if n == 1:return 0
        else:
            return (self.LastRemaining_Solution(n-1,m)+m)%n 
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not m or not n:
            return -1
        res = list(range(n))
        i = 0
        while len(res)>1:
            i = (m+i-1)%len(res)
            res.pop(i)
        return res[0]

s = Solution()
print(s.LastRemaining_Solution(4000,997))


