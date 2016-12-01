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
    elif n > 3:
        value = fib(t1, t2, n - 2) + fib(t1, t2, n - 1) ** 2 
    else:
        value = t1 + t2 ** 2
        
        
    return value

t1, t2, n = map(long, raw_input().strip().split(" "))

print fib(t1, t2, n)

