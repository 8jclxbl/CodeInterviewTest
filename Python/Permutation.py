def Permutation(ss):
        # write code here
    if not ss: return ''
    res = [ss[0]]
    for ch in ss[1:]:
        length = len(res[0])
        temp = []
        for i in res:
            for j in range(length+1):
                if j == length:temp.append(i + ch)
                else:temp.append(i[0:j] + ch + i[j:])
        res = list(set(temp))
    return sorted(res)


print(Permutation('aab'))