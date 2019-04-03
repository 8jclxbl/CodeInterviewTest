<<<<<<< HEAD
=======
"""
当模式中的第二个字符不是“*”时：
1、如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的。
2、如果 字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。

而当模式中的第二个字符是“*”时：
如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，继续匹配。如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
1、模式后移2字符，相当于x*被忽略；
2、字符串后移1字符，模式后移2字符；
3、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位；
"""

>>>>>>> 2892259d1f4abee4f65d0332f60651a734fabe72
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
<<<<<<< HEAD
        ls = len(s)
        lp = len(pattern)
        if ls == 0 and lp == 0:
            return True
        if ls > 0 and lp == 0:
            return False
        if lp > 1 and pattern[1] == '*':
            if ls > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return (self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern))
            else:
                return self.match(s, pattern[2:])
        if ls > 0 and (pattern[0] == '.' or pattern[0] == s[0]):
            return self.match(s[1:], pattern[1:])
        return False
=======
        pl = len(pattern)
        if s == '':
            if pattern == '' or (pl == 2 and pattern[1] == '*') :return True
            else: return False
        else:
            if pl > 1:
                if pattern[1] != '*':
                    if s[0] == pattern[0]:return self.matchp(s[1:],pattern[1:])
                    else:return False
                else:
                    if s[0] != pattern[0]:return self.match(s,pattern[2:])
                    else:
                        return self.match(s,pattern[2:]) or self.match(s[1:],pattern[2:]) or self.match(s[1:],pattern)  
            else:
                return False      

test_s = ['aaa','aaa','aaa','aaa']
test_p = ['a.a','ab*ac*a','aa.a','ab*a']

s = Solution()
"""
for i,j in zip(test_s,test_p):
    print(s.match(i,j))
"""

print(s.match("aa",".*"))
>>>>>>> 2892259d1f4abee4f65d0332f60651a734fabe72
