'''
Created on Nov 17, 2016

@author: erexsha
'''
target = int(raw_input().strip())
count = int(raw_input().strip())
arr = map(int, raw_input().strip().split(" "))

found = False
bottom = 0
top = count - 1
index = (top + bottom) / 2
while not found and index >= bottom and index <= top:
    if target < arr[index]:
        top = index
        newindex = (top + bottom) / 2
        if newindex == index:
            index -= 1
        else:
            index = newindex    
    elif target > arr[index]:
        bottom = index
        newindex = (top + bottom) / 2
        if newindex == index:
            index += 1
        else:
            index = newindex    
    else:
        found = True
        
print index