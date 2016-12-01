# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Created on Nov 28, 2016

@author: erexsha
'''

def max_stock(prices):
    
    max = 0
    profit = 0
    
    for price in reversed(prices):
        if price > max:
            max = price
        profit += max - price
    
    return profit

tc = int(raw_input().strip())

for i in range(tc):
    n = int(raw_input().strip())

    prices = map(int, raw_input().strip().split(" "))
    
    print max_stock(prices)