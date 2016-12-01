# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
Created on Nov 22, 2016

@author: erexsha
'''


def find_coin(t, coin, soln, solns):
    
    found = False
    for i in coin:
        remain = t - i
        soln.append(i)
        if remain > 0:
            find_coin(remain, coin, soln, solns)
        elif remain == 0:
            s = " ".join(str(e) for e in sorted(soln))
            solns[s] = 1
#            print soln
        else:
            soln.pop()
            break

        soln.pop()
            
    
    return found

target, n = map(int, raw_input().strip().split(" "))
coin = map(int, raw_input().strip().split(" "))

soln = [] 
solns = {}

c = sorted(coin)

find_coin(target, c, soln, solns)

print str(len(solns))