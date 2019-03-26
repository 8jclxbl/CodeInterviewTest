def reOrderArray_me(array):
    l = len(array)
    i = 0
    last = -1
    while i < l:
        if array[i] % 2 == 1:
            if i != last:
                j = i
                while j - 1 > last:
                    array[j],array[j-1] = array[j-1],array[j]
                    j -= 1
                last += 1
        i += 1
    return array

def reOrderArray_best(array):
        # write code here
        odd = deque()
        x = len(array)
        for i in range(x):
            if array[x-i-1]%2 != 0:
                odd.appendleft(array[x-i-1])
            if array[i]%2 == 0:
                odd.append(array[i])
        return list(odd)

    
print(reOrderArray_me([1,2,3,4,5,6]))

