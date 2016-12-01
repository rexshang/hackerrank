'''
Created on Nov 22, 2016

@author: erexsha
'''
memo = {}

def find_coin(t, coin, soln, solns):
    
    ways = 0
    for i in coin:
        remain = t - i
        soln.append(i)
        if remain > 0:
            if remain in memo.keys():
                ways = memo[remain]
            else:
                length = len(coin)
                newcoin = coin[1: length - 1]
                memo[remain] = find_coin(remain, newcoin, soln, solns)
        elif remain == 0:
            s = " ".join(str(e) for e in sorted(soln))
            solns[s] = 1
            ways += 1
#            print soln
        else:
            soln.pop()
            break

        soln.pop()
            
    
    return ways

target, n = map(int, raw_input().strip().split(" "))
coin = map(int, raw_input().strip().split(" "))

soln = [] 
solns = {}

c = reversed(sorted(coin))

find_coin(target, c, soln, solns)

print str(len(solns))