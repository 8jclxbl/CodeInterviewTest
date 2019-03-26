def duplicate(numbers, duplication):
        # write code here
        dic = {}
        
        for i in numbers:
            if i in dic:
                duplication[0] = i
                print(i)
                return True
                
            else:
                dic[i] = 1
        return False

def bestDuplicate(numbers, duplication):
    length = len(numbers)
    for i in range(length):
        if numbers[i] >= length:
            idx = numbers[i] - length
        else:
            idx = numbers[i]

        if numbers[idx] >= length:
            duplication[0] = idx
            return True
        else:
            numbers[idx] += length
    return False

d = [1]
print(duplicate([2,1,3,2,4],d))
print(d)
print(bestDuplicate([2,1,3,2,4],d))
print(d)