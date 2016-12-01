'''
Created on Nov 7, 2016

@author: erexsha
'''
#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


neg = 0
_pos = 0
zero = 0
total = float(len(arr))

for l in arr:
    if l < 0:
        neg = neg + 1
    elif l == 0:
        zero = zero + 1
    else:
        _pos = _pos + 1
neg_numbers = neg / total
pos_numbers = _pos / total
zero_numbers = zero / total

print(pos_numbers)
print(neg_numbers)
print(zero_numbers)