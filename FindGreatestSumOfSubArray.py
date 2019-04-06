class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        cur_sum = array[0]
        max_sum = cur_sum
        length = len(array)
        for i in range(1,length):
            cur_sum = max(array[i], array[i] + cur_sum)
            if cur_sum > max_sum: max_sum = cur_sum
        return max_sum

s = Solution()
print(s.FindGreatestSumOfSubArray([-2,-8,-1,-5,-9]))