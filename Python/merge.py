"""inverse = 0
def seprate(data):
    if not data: return None
    length = len(data)
    if length == 1: return [data]
    else:
        return seprate(data[0:length//2]) + seprate(data[length//2:])

def total(data):
    length = len(data)
    if not length: return None
    if length == 1: return data[0]
    else:
        res = []
        if length % 2 == 0: l = length
        else: l = length - 1
        for i in range(0,l,2):
            res.append(mearge(data[i],data[i+1]))
        if l != length:res.append(mearge([],data[l]))
        return total(res)

def mearge(d1,d2):
    global inverse
    if not d1 and not d2:
        return []
    l1 = len(d1)
    l2 = len(d2)
    i = 0
    j = 0
    res = []
    while True: 
        if i >= l1:     
            res += d2[j:]
            break
        if j >= l2: 
            res += d1[i:]
            break

        if d1[i] > d2[j]:
            inverse += len(d1[i:])
            res.append(d2[j])
            j += 1
        else:
            res.append(d1[i])
            i += 1

    return res
"""

class Solution:
    inverse = 0
    def InversePairs(self, data):
        self.total(self.seprate(data))
        return self.inverse%1000000007
        # write code here
    def seprate(self,data):
        if not data: return None
        length = len(data)
        if length == 1: return [data]
        else:
            return self.seprate(data[0:length//2]) + self.seprate(data[length//2:])

    def total(self,data):
        length = len(data)
        if not length: return None
        if length == 1: return data[0]
        else:
            res = []
            if length % 2 == 0: l = length
            else: l = length - 1
            for i in range(0,l,2):
                res.append(self.mearge(data[i],data[i+1]))
            if l != length:res.append(self.mearge(data[l],[]))
            return self.total(res)

    def mearge(self,d1,d2):
        if not d1 and not d2:
            return []
        l1 = len(d1)
        l2 = len(d2)
        i = 0
        j = 0
        res = []
        while True: 
            if i >= l1:     
                res += d2[j:]
                break
            if j >= l2: 
                res += d1[i:]
                break

            if d1[i] > d2[j]:
                self.inverse += len(d1[i:])
                res.append(d2[j])
                j += 1
            else:
                res.append(d1[i])
                i += 1
        return res

s = Solution()
test = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
print(s.InversePairs(test))
    