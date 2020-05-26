from collections import Counter
import sys
liners = []
str = sys.stdin.readlines()
for chisla in str:
    liners.append(chisla)
#print(liners)


mylist = []
for b in str:
     mylist.append(b)
     #print(mylist)
k = 0
v = 0

for k,v in Counter(mylist).items():
    #print(Counter(mylist))
    if v < 2:
        #print(k)
        sys.stdout.write(k)



