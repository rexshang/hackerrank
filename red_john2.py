# Enter your code here. Read input from STDIN. Print prime to STDOUT

'''
Created on Dec 8, 2016

@author: erexsha
'''

import math

memo = {}
primes = {}

last_prime = 0
prime_cnt = 0

def find_primes(upper):
    global last_prime
    global prime_cnt
    
    #combo = 217286
    for num in range(last_prime, upper + 1):
        # prime_cnt numbers are greater than 1
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if (num % i) == 0:
                    break
            else:
                prime_cnt += 1
        primes[num] = prime_cnt
        
    last_prime = upper + 1
    
    
def find_ways(n):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    elif n < 4:
        return 1
    else:
        
        if (n-4) in memo:
            f4 = memo[n-4]
        else:
            f4 = find_ways(n-4)
            memo[n-4] = f4
            
        if (n-1) in memo:
            f1 = memo[n-1]
        else:
            f1 = find_ways(n-1)
            memo[n-1] = f1
            
        ways = f4 + f1
        memo[n] = ways           
        return ways

memo[1] = 1
memo[2] = 1
memo[3] = 1
memo[4] = 2

find_primes(101)

tc = int(raw_input().strip())

for _ in range(tc):
    target= int(raw_input().strip())
    
    ways = find_ways(target)
    if ways > last_prime:
        find_primes(ways)
        
    #print ways
    print primes[ways]
    
