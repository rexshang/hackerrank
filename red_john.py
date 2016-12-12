# Enter your code here. Read input from STDIN. Print prime to STDOUT

'''
Created on Dec 8, 2016

@author: erexsha
'''
memo = {}

def find_coin(t, coin, soln, solns):
    
    ways = 0
    for i in coin:
        remain = t - i
        soln.append(i)
        if remain > 0:
            #if remain in memo.keys():
            #    ways += memo[remain]
            #else:
            #memo[remain] = find_coin(remain, coin, soln, solns)
            ways += find_coin(remain, coin, soln, solns)
        elif remain == 0:
            s = ''.join(str(e) for e in soln)
            solns[s] = 1
            ways += 1
#            print soln
        else:
            coin = coin[1:]
            #soln.pop()
            #break
        soln.pop()
            
    
    return ways

tc = int(raw_input().strip())

for _ in range(tc):
    target= int(raw_input().strip())
    
    coin = [4, 1]
    
    soln = []
    solns = {}
    
    find_coin(target, coin, soln, solns)
    print "combo: " +  str(len(solns))
    print solns
    combo = len(solns)
    
    prime = 0
    for num in range(0, combo + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                prime += 1
    print prime