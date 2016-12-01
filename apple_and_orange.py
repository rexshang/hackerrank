'''
Created on Nov 8, 2016

@author: erexsha
'''
#!/bin/python

import sys

def count_fruit(s, t, tree, fruit):
    count = 0
    for i in fruit:
        dist = i + tree
        if dist >= s and dist <= t:
            count = count + 1
    return count
    
s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

        
print count_fruit(s, t, a, apple)
print count_fruit(s, t, b, orange)
    