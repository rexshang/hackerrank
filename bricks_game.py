# Enter your code here. Read input from STDIN. Print prime to STDOUT

'''
Created on Dec 8, 2016

@author: erexsha
'''


tc = int(raw_input().strip())

for _ in range(tc):
    datalength = int(raw_input().strip())
    
    bricks = map(int, raw_input().strip().split(' '))
    
    start = 0
    total = 0
    a_turn = True
    
    lookahead = start + 6
    
    while datalength > 0:
        myview = [0]*6
        j = 0
        for i in range(0, 6):
            if i >= datalength:
                pass
            #myview[j] = 0
            else:
                myview[j] = bricks[i]
            j += 1
            
        a = myview[0] + myview[1] + myview[2]
        b = myview[0] + myview[1] + myview[5]
        c = myview[0] + myview[4] + myview[5]
        
        if a >= b:
            if a >= c:
                #a greater; take 3 bricks
                for _ in range(3):
                    datalength -= 1
                    if datalength >= 0:
                        del(bricks[0])
                    
                if a_turn:
                    total += a
                
            else:
                #c greater
                #take 1 brick
                if a_turn:
                    total += bricks[0]
                datalength -= 1
                del(bricks[0])
                
        else:
            if b >= c:
                #b greater, take 2 bricks
                if a_turn:
                    total += bricks[0] + bricks[1]
                for _ in range(2):
                    datalength -= 1
                    if datalength >= 0:
                        del(bricks[0])
                
            else:
                #c greater; take 1 brick
                datalength -= 1
                del(bricks[0])
                if a_turn:
                    total += c
                
            
        if a_turn == True:
            a_turn = False
        else:
            a_turn = True      
    
    print total