'''
Created on Nov 4, 2016

@author: erexsha
'''

import sys


n = long(raw_input().strip())
count = 0

if n == 0: count = 1
i = long(0)

while i < n:
    #sum = n + i
    #xor = n ^ i
    dif = (n ^ i) - n - i 
#    xor = (n or i) and not (n and i)
    if dif == 0:#sum == xor:
        count = count + 1
    i = i + 1
print count