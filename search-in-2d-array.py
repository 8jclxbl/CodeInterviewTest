def Find(target, array):
    r = len(array)
    c = len(array[0])

    if c == 0: return False

    for i in range(r):
        if array[i][-1] >= target:
            lo = 0
            hi = c-1
            
            while lo < hi:
                mid = (lo + hi)//2
                if array[i][mid] > target:
                    hi = mid-1
                elif array[i][mid] < target:
                    lo = mid+1
                else:
                    return True

    return False
