def PrintMinNumber(numbers):
    str_num = [str(i) for i in numbers]
    length = len(numbers)
    f = lambda x,y:x + y > y + x
    k = 1
    while length - k > 0:
        i = 0
        changed = False
        while i < length - k:
            if f(str_num[i],str_num[i+1]):
                changed = True
                str_num[i],str_num[i+1] = str_num[i+1],str_num[i]
            i += 1
        if not changed:break
        k += 1
    return ''.join(str_num)
print(PrintMinNumber([3,32,321]))
