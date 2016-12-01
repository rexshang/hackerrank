'''
Created on Nov 29, 2016

@author: erexsha
'''

def fill(i, j):
    global mat
    
    if i < 0 or j < 0 or i >= n or j >= m or mat[i][j] == 0 or mat[i][j] == -1:
        return 0
    else:
        mat[i][j] = -1
        
        return 1 + fill(i-1, j-1) + fill(i-1, j) + fill(i-1, j+1) + fill(i, j+1) + fill(i+1, j+1) + fill(i+1, j) + fill(i+1, j-1) + fill(i, j-1)
        

n = int(input())
m = int(input())

mat = []

for i in range(n):
    line = map(int, raw_input().split(" "))
    mat.append(line)

area = 0    
for i in range(n):
    for j in range(m):
        area = max(area, fill(i, j))
        
print area