# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Created on Dec 1, 2016

@author: erexsha
'''

def morepath(mat, n, m):
    
    path = 0
    if m-1 >= 0 and mat[n][m-1] == '.':
        path += 1
    if m+1 < col and mat[n][m+1] == '.':
        path += 1
    if n-1 >=0 and mat[n-1][m] == '.':
        path += 1
    if n+1 < row and mat[n+1][m] == '.':
        path += 1
        
    return path


def findport(n, m):
    global out
    global mat_bk
 
    if out == True or n < 0 or m < 0 or n >= row or m >= col or mat[n][m] == 'X' or mat[n][m] == 'o':
        return 0
    elif mat[n][m] == '*':
        mat_bk[n][m] = '.'
        out = True
        return 0
    else:
        mat[n][m] = 'o'
        weight = 1 + findport(n, m-1) + findport(n, m+1) + findport(n-1, m) + findport(n+1, m)
        
        if out == True:
            st.append([n, m])

        return weight

tc = int(raw_input())
row = 0
col = 0
mat = []
mat_bk = []
st = []
out = False

for _ in range(tc):
    n, m = map(int, raw_input().split(' '))
    row = n
    col = m
    
    mat = []
    mat_bk = []

    for i in range(n):
        line = raw_input()
        mat_bk.append(list(line))
        mat.append(list(line))
        
    k = int(raw_input())
    #print mat
    
    found = 0
    out = False
    st = list()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 'M':
                mat_bk[i][j] = '.'
                found = findport(i,j)
                break
        else:
            continue
        break
    #print st
    
    #print mat
    
    found = 0
    # check the exit node
    #[i, j] = st[0]
    #if morepath(mat_bk, i, j) > 1:
    #    print [i, j]
    #    found += 1
    # check the beginning node
    [i, j] = st.pop()
    if morepath(mat_bk, i, j) > 1:
        #print [i, j]
        found += 1
    for [i, j] in st:
        if morepath(mat_bk, i, j) > 2:
            #print [i, j]
            found += 1
        
    #print found
    if found == k:
        print ("Impressed")
    else:
        print ("Oops!")
    