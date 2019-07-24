def LomutiPartition(A):
    length = len(A)
    p = A[0]
    s = 0   
    #s 是G区和L区的划分点
    for i in range(1,length):
        #若大于p则s的位置不动，指针前移，相当于把当前元素加入大于区
        if A[i] < p:
            #此时元素应该加入小于区，s+1会将原属于大于区的一个元素加入小于区，之后将要加入小于区的元素与之交换，达到标准状态
            s += 1
            A[i],A[s] = A[s],A[i]
    A[0],A[s] = A[s],A[0]
    return s

def HoarePartition(A):
    length = len(A)
    p = A[0]
    lo = 1
    hi = length - 1

    while lo < hi:
        while A[lo] <= p: lo += 1
        while A[hi] >= p: hi -= 1
        A[lo],A[hi] = A[hi],A[lo]
    A[lo],A[hi] = A[hi],A[lo]
    A[0],A[hi] = A[hi],A[0]
    return hi

def QuickSelect(k,A):
    s = LomutiPartition(A)
    if s == k-1:return A[s]
    elif s > k-1:
        return QuickSelect(k,A[:s])
    else:
        return QuickSelect(k-s-1,A[s+1:])

if __name__ == "__main__":

    A = [3,1,2,4,5,6]
#print(LomutiPartition(A))
    print(HoarePartition(A))
#print(QuickSelect(6,A))