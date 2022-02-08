# -*- coding: utf-8 -*-
import random as rnd
import time

wscore = 0 #White/Black score
bscore = 0
for i in range(100):
    figures = ['Q', 'B', 'R']
    pawns=['_' for i in range (61)] + figures
    rnd.shuffle(pawns)
    board = [pawns[i:i+8] for i in range(0, len(pawns),8)]


    def findpos(p,cpos,board): #Find where each pawn(Q,B,R) can move to, cpos=current position
        ppos = [] #possible position
        i,j = cpos[0],cpos[1]
        if (p == 'Q' or p == 'R'):
            for hor1 in range(j+1,8): # Check horizontally
                ppos.append((board[i][hor1]))
            for hor2 in range(j-1,-1,-1): 
                ppos.append((board[i][hor2]))
            for ver1 in range(i+1,8): # Check vertically
                ppos.append((board[ver1][j]))
            for ver2 in range(i-1,-1,-1):
                ppos.append((board[ver2][j]))
        if (p == 'Q' or p == 'B'):
            k=0
            for drd in range(j+1,8): # Down-right diagonal
                k+=1
                if (i+1+k>8):
                    break
                ppos.append(board[i+k][drd])
            k=0
            for dld in range(j-1,-1,-1): # Down-left diagonal
                k+=1
                if (i+1+k>8):
                    break
                ppos.append(board[i+k][dld])
            k=0
            for urd in range(j+1,8): # Upper-right diagonal
                k-=1
                if (i+1+k<1):
                    break
                ppos.append(board[i+k][urd])
            k=0
            for uld in range(j-1,-1,-1): # Upper-left diagonal
                k-=1
                if (i+1+k<1):
                    break
                ppos.append(board[i+k][uld])
        return ppos 


    for pawn in board:
        for j in range (8):
            if (pawn[j]=='Q'):
                p = 'Q'
                qpos = (board.index(pawn),j) #Get the queens position
                possibleq = findpos(p,qpos,board)
            elif (pawn[j]=='B'):
                p = 'B'
                bpos = (board.index(pawn),j) #Get the bishops position
                possibleb = findpos(p,bpos,board)
            elif (pawn[j]=='R'):
                p = 'R'
                rpos = (board.index(pawn),j) #Get the rooks position
                possibler = findpos(p,rpos,board)

    for line in board: #Print the board clearly for aesthetic purposes
        print (line)

    print (f"The Queen is located at {qpos}. \nThe Bishop is located at {bpos}. \nThe Rook is located at {rpos}.")
    possiblewhite = possibleb + possibler # To easily access the list without having to do two seperate loops later

    for pawn in possibleq:
        if (pawn != '_'):
            bscore += 1
    for pawn in possiblewhite:
        if (pawn == 'Q'):
            wscore += 1
print('################################################')
print('\nCalculating results..\n')
time.sleep(3)
print(f"White\'s total score: {wscore}. \nBlack\'s total score: {bscore}.\n")
input("Press any button to continue.. \n")
