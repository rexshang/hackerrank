'''
Created on Nov 18, 2016

@author: erexsha
'''

def max(a, b):
    if a > b:
        return a
    else:
        return b

def findmaxsub(array):
    current_max = array[0] 
    absolute_max = array[0]
    nc_max = array[0]
    
    for i in range(1, len(array)):
        current_max = max(array[i], current_max + array[i])
        # in case of all neg numbers, current value may be the max sum
        absolute_max = max(absolute_max, current_max)
        
        
        nc_max = max(nc_max, nc_max + array[i])
        # in case of all neg numbers, current value may be the max sum
        nc_max = max(array[i], nc_max)

    return [absolute_max, nc_max]


tc = int(raw_input().strip())

for testcase in range(tc):
    length = int(raw_input().strip())
    
    if length > 0:
        arr = map(int, raw_input().strip().split(" "))
    
    #print max_subarray(arr)
    output = findmaxsub(arr)
    
    print " ".join(str(e) for e in output)