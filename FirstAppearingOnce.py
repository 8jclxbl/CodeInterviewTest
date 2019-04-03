# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.data = []
        self.tail = -1
        self.dict = {}
        self.cur = -1

    def FirstAppearingOnce(self):
        # write code here
        if self.tail == -1: return '#'
        if self.tail == 0: 
            self.cur = 0
            return self.data[0]
        while self.cur < self.tail:
            if self.data[self.cur] not in  self.dict:self.cur += 1
            else: break
        if self.cur == self.tail and not self.dict: return '#'
        return self.data[self.cur]

    def Insert(self, char):
        # write code here
        self.data.append(char)
        self.tail += 1
        if char in self.dict:
            del(self.dict[char])
        else:
            self.dict[char] = 1

s = Solution()
for i in 'google':
    s.Insert(i)
    print(s.FirstAppearingOnce(),s.data,s.dict)

