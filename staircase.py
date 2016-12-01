'''
Created on Nov 7, 2016

@author: erexsha
'''
import sys

n = int(raw_input().strip())

for i in range(n):
    print " " * (n - i - 1) + "#" * (i + 1)
