import itertools
a = 5
b = [1, 7, 3, 4, 7, 9]

comb = list(itertools.combinations(b, 2))

result = list(map(sum, comb))

#print(1 if a in result else 0)
data = []
with open("input.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])

if a in result:
    print("1")


else :
    print("0")