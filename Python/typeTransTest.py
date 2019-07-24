import timeit

func1 = """
def compute(x,y):
    x = str(x)
    y = str(y)
    sum = 0
    for i in x+y:
        sum += int(i)
    return sum
a = compute(100,100)
"""

func2 = """
def compute(x):
    sum = 0
    while x:
        sum += x % 10
        x = x // 10
    return sum
a = compute(100) + compute(100)
"""

print(timeit.timeit(func1,number=1000))

print(timeit.timeit(func2,number=1000))