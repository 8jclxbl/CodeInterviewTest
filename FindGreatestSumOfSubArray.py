def FindGreatestSumOfSubArray(array):
    length = len(array)
    sum = a[0]
    i = 1
    while i < length:
        temp = sum + array[i]
        if temp > sum:
            sum = temp
        i += 1

        
        