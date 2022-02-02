import collections
from string import ascii_letters

def freqFind(list,n):
    wordcount = collections.Counter(list) #Creates a dictionary with the each word and its frequency
    return (wordcount.most_common(n))


f = open("two_cities_ascii.txt", "r")

allowedchars = list(ascii_letters + ' ')
data = f.read().replace('\n', ' ')
for i in range(128):
    if (chr(i) not in allowedchars):
        data = data.replace(chr(i), "")

words = data.split(' ')
words = list(filter(None, words)) #Remove all empty spaces

for word in range (len(words)):
    words[word] = words[word].lower()

w2 = [word[:2] for word in words if len(word)>1] #Words starting with 2/3
w3 = [word[:3] for word in words if len(word)>2]
mostcommon10 = freqFind(words,10)
mostcommon2 = freqFind(w2,3)
mostcommon3 = freqFind(w3,3)

print(f"\nThe 10 most popular words are:\n {mostcommon10}\n")
print(f"\nThe 3 most popular first 2-letters are:\n {mostcommon2}\n")
print(f"\nThe 3 most popular first 3-letters are:\n {mostcommon3}\n")

input('Press any button to continue..\n')
f.close()