def GetLeastNumbers(tinput, k):
        # write code here
        length = len(tinput)
        count = 1
        temp = [tinput[0]]
        for i in range(1,length):
            inSerted = False
            for j in range(count):
                if tinput[i] < temp[j]:
                    temp.insert(j,tinput[i])
                    inSerted = True
                    break
            if not inSerted: temp.append(tinput[i])
            count += 1
        return temp[:k]

print(GetLeastNumbers([4,5,1,6,2,7,3,8],4))