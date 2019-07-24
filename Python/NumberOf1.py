class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        order = 1
        while order <= n:
            count += (n // order + 8) // 10 * order + (n // order % 10 == 1) * (n % order + 1)
            order *= 10
        return ones