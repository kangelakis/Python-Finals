f = open("two_cities_ascii.txt", "r")
try:
    data = f.read().replace('\n', '')
    words = list(data)
    for i in range (len(words)):
        words[i] = (format(ord(words[i]), 'b')) #Turn each character of the list into its binary form 
        words[i] = (7-len(words[i]))*'0' + words[i] # If a binary code is less than 7 bits add 0s' to the end of it

    sequence = "".join(words)
    c0,c1 = 0,0 #Count 0,1
    s0,s1 = c0,c1 #Sequence 0,1
    for bit in sequence:
        if bit=='0':
            c0+=1
            if(s1<c1):
                s1=c1
            c1=0
        else:
            c1+=1
            if(s0<c0):
                s0=c0
            c0=0
    print(f"\nThe max 0 sequence was {s0}. \nThe max 1 sequence was {s1}.")
except:
    print('\nThe file doesn\'t have any contents.')
f.close()
input("\nPress any button to continue.. \n")