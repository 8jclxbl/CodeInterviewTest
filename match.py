class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
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
