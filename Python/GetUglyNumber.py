def GetUglyNumber(index):
    if index < 7: return index
    else:
        temp = [1]
        
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range(index-1):
            temp.append(min(temp[i2] * 2,temp[i3] * 3,temp[i5] * 5))
            if temp[-1] == temp[i2] * 2: i2 += 1
            if temp[-1] == temp[i3] * 3: i3 += 1
            if temp[-1] == temp[i5] * 5: i5 += 1
        return temp

print(GetUglyNumber(100))    