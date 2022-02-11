import random,time

nw1 = 0 #Normal win for p1 etc for the rest
nw2 = 0
ndr = 0
print ("-----Normal Shuffle-----")
for r in range(100):
    
    print(f"Normal Round {r+1}")
    #time.sleep(1) 
    print ("Shuffling..")
    #time.sleep(2)
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        print(f"Player 1 picks a card: {card[0]}")
    print(f"Player 1's sum = {sum1}")
    if sum1>21:
        print("P2 wins!")
        nw2 += 1
    else:
        print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            print(f"Player 2 picks a card: {card[0]}")
        print(f"Player 2's sum = {sum2}")
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            nw1 += 1
        elif sum2>sum1:
            print("P2 wins!")
            nw2 += 1
        else:
            print("draw!")
            ndr += 1
        print("#########################")




cw1 = 0
cw2 = 0
cdr = 0
print ("-----Cheat Shuffle-----")
for r in range(100):
    print(f"Cheat Round {r+1}")
    #time.sleep(1) 
    print ("Shuffling..")
    #time.sleep(2)
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    cheatcards= [10, "J", "K", "Q"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    firstpick = True
    while sum1<16:
        sum1=0
        if (firstpick): # Simple block that searches and appends the first card of value 10 to player1
            for firstpoints in xartia:
                if firstpoints[0] in cheatcards:
                    player1.append(firstpoints)
                    xartia.remove(firstpoints)
                    firstpick = False
                    break
        else:
            player1.append(xartia.pop())
        
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        print(f"Player 1 picks a card: {card[0]}")
    print(f"Player 1's sum = {sum1}")
    if sum1>21:
        print("P2 wins!")
        cw2 += 1
    else:
        print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            for no10s in xartia:
                if ((no10s[0] not in cheatcards) or player2!=[]): #Don't append a card of value 10 to P2 in the 1st round only
                    player2.append(no10s)
                    xartia.remove(no10s)
                    break

            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            print(f"Player 2 picks a card: {card[0]}")
        print(f"Player 2's sum = {sum2}")
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print("P1 wins!")
            cw1 += 1
        elif sum2>sum1:
            print("P2 wins!")
            cw2 += 1
        else:
            print("draw!")
            cdr += 1
        print("#########################")
print ("Calculating Results..\n")
time.sleep(3)
print(f"Player 1 | Normal round wins: {nw1} | Cheat round wins: {cw1}. \nPlayer 2 | Normal round wins: {nw2} | Cheat round wins: {cw2}. \nDraw | Normal round occurences: {ndr} | Cheat round occurences {cdr}.")
input("\nPress any button to continue.. \n")