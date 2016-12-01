'''
Created on Nov 4, 2016

@author: erexsha
'''

#!/usr/bin/py
def lonelyinteger(a):
    data = {}
    for i in a:
        if data.has_key(i):
            del(data[i])
        else:
            data[i] = 1
    l = list(data.keys())
    answer = l[0]
    #print answer
    return answer

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
        
