def multiply(A):
        # write code here
        length = len(A)
        left = [1]
        right = [1]
        for i in range(length-1):
            j = length - 1 - i
            left.append(left[-1] * A[i])
            right.insert(0,right[0] * A[j])
        res = []
        print(left,right)
        for i in range(length):
            res.append(left[i]*right[i])
        return res

print(multiply([1,2,3,4,5]))