def FindNumsAppearOnce(array):
        # write code here
        temp = {} 
        for i in array:
            if i in temp:
                del temp[i]
            else:
                temp[i] = 1
        return temp.keys()

def FindNumsAppearOnce(self, array):
        # write code here
        result = 0
        for obj in array:
            result ^= obj    # 异或运算，剩下的是a,b不同的两个数的异或结果
        index = self.find_1_index(result)
        num1 ,num2 = 0, 0
        for obj in array:
            if self.is_bit_1(obj, index):
                num1 ^= obj        # 第N位为1的分为1组，因为这样能保证a,b分为两组
            else:
                num2 ^= obj
        return num1, num2
 
    def find_1_index(self, digit):
        """找到右边第一个为1的位置,右移和位与运算
 
        :param digit:
        :return:
        """
        index = 0
        while not digit & 1:
            digit >>= 1
            index += 1
        return index
 
    def is_bit_1(self, digit, n):
        """判断某个数字的右边的第n位是否为1
 
        :param s:
        :param n:
        :return:
        """
        digit >>= n
        return digit & 1     # 位与运算

print(FindNumsAppearOnce([1,2,3,4,5,4,3,1]))