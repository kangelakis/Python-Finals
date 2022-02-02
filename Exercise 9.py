f = open("two_cities_ascii.txt", "r")
try:
    data = f.read().replace('\n', '')
    words = list(data)
    for i in range (len(words)):
        words[i] = (format(ord(words[i]), 'b')) #Turn each character of the list into its binary form 
        words[i] = (7-len(words[i]))*'0' + words[i] # If a binary code is less than 7 bits add 0s' to the end of it

    bina =[]

    for word in words:
        word = list(word)
        bina.append(word)
        #print(word) prints every word in binary
        
    lst0 =[]
    lst1= []
    for i in bina: # For each 7-bit binary
        c0 = 0
        t0 = c0 
        c1 = 0
        t1 = c1
        for j in range (7): # For each bit 
            if (i[j] == '0'):
                c0 += 1
                if (t1 < c1): #t1 as well as t0 are temporary variables used to store c1's/c0's value before it reaches a 0/1
                    t1 = c1 
                c1 = 0
            else: # vice versa
                c1 += 1
                if (t0 < c0):
                    t0 = c0 
                c0=0
        if (t0 > c0):
            c0 = t0
        if (t1 > c1):
            c1 = t1
        lst0.append(c0)
        lst1.append(c1)

    print(f"\nThe max 0 sequence was {max(lst0)}. \nThe max 1 sequence was {max(lst1)}.")
except:
    print('\nThe file doesn\'t have any contents.')
f.close()
input("\nPress any button to continue.. \n")