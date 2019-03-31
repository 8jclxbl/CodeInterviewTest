class Solution:
    # s字符串
    #ord('+') 43
    #ord('-') 45

    def isNumeric(self, s):
        # write code here
        length = len(s)
        if not((s[0] >= '0' and s[0] <= '9') or s[0] == '+' or s[0] == '-'):return False

        pE = -1
        pDot = -1
        i = 1
        while i < length:
            if s[i] == 'e' or s[i] == 'E': 
                if pE == -1:
                    pE = i
                    if i == length - 1: return False
                    if (s[i+1] >= '0' and s[i+1] <= '9') or s[i+1] == '-' or s[i+1] == '+':
                        i += 2
                        continue
                    return False
                return False

            
            if s[i] == '.': 
                if pE != -1 and i > pE: return False
                if pDot == -1:
                    
                    pDot = i
                    i += 1
                    continue
                else:
                    return False

            if (s[i] >= '0' and s[i] <= '9'):
                i += 1
            else:return False
        
        return True
            
test = ["+100","5e2","-123","3.1416","-1E-16","12e","1a3.14","1.2.3","+-5","12e+4.3"]
s = Solution()
for i in test:
    print(i, s.isNumeric(i))
#print(s.isNumeric("1.2.3"))

