'''
Created on Nov 28, 2016

@author: erexsha
'''

from sets import Set

def max(a, b):
    if a > b:
        return a
    else:
        return b

def knapsack(target, elements, index):
    if target <= 0:
        return 0
    
    weight = elements[index]
    # inc vs not inc
    
    multiple = 0
    product = 0
    maximum = 0
    
    if index == 0:
        remainder = target % weight
        if remainder == 0:
            return target
        else:
            return target - remainder
        
    while product < target and target > maximum:
        val = knapsack(target - product, elements[0:index], index - 1) + product     
        maximum = max(val, maximum)
        multiple += 1
        product = multiple * weight
 
    return maximum


tc = int(raw_input().strip())

for i in range(tc):
    n, target = raw_input().strip().split(" ")
    n, target = [int(n), int(target)]

    elem = map(int, raw_input().strip().split(" "))
    
    e_set = Set(elem)
    l = sorted(list(e_set))
    
    print knapsack(target, l, len(l) - 1)