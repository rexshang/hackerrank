'''
Created on Nov 17, 2016

@author: erexsha
'''
def fib(t1, t2, n):
    value = long(0)
    if n < 3:
        if n == 1:
            value = t1
        elif n == 2:
            value = t2
        else:
            value = 0
    else:
        for _ in range(2, n):
            value = t1 + t2 ** 2
            t1 = t2
            t2 = value

    return value

t1, t2, n = map(long, raw_input().strip().split(" "))

print fib(t1, t2, n)