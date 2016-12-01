'''
Created on Nov 11, 2016

@author: erexsha
'''


n = int(raw_input().strip())

arr1 = map(str,raw_input().strip().split(' '))

dic = dict()
for num in arr1:
    if num in dic:
        dic[num] = dic[num] + 1
    else:
        dic[num] = 1
            
#print dic

m = int(raw_input().strip())

sorted_list = set()
arr2 = map(str,raw_input().strip().split(' '))
for num in arr2:
    if num in dic:
        dic[num] = dic[num] - 1
        if dic[num] == 0:
            del dic[num]
    else:
        sorted_list.add(num)
        
#for key in dic:
#    sorted_list.add(key)
            
            
#sorted_list.sort()
output = " ".join(sorted(sorted_list))
print output