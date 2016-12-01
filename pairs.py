'''
Created on Nov 14, 2016

@author: erexsha
'''

import sys
import cProfile

def pairs(a,k):
    answer = 0
    
    length = len(a)
    #a.sort()
    b = {}
    for left in range(length):
        b[a[left]] = ' '
    
    for left in range(length):
        diff1 = a[left] + k 
        diff2 = a[left] - k 
        if diff1 in b:
            answer = answer + 1
        if diff2 in b:
            answer = answer + 1     
        
    return answer / 2

a, k = map(int, raw_input().strip().split(' '))
num = map(int, raw_input().strip().split(' '))

#print a
#print k 
#print num
def main():
    print pairs(num,k)
    
cProfile.run('main()')