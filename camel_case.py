'''
Created on Nov 8, 2016

@author: erexsha
'''
import sys


s = raw_input().strip()
r = range(ord('A'), ord('Z') + 1)
r1 = range(ord('a'), ord('z') + 1)

count = 1
for char in s:
    #print ord(char)
    if (ord(char) in r):
#    if (ord(char) >= ord('A')  and ord(char) <= ord('Z')):
        count = count + 1
    elif (ord(char) in r1):
        noop = 0
    else:
        print "error: " + char

print count