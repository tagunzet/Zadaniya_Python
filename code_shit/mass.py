mass = [1,2,3,4,5,6,7,8,9]
out = []
i = 0
g = 1
k = 2
while i <= len(mass)-1:
    one = mass[i] + 0
    i = i + 3
    print(one)
    out.append(one)
while g <= len(mass)-1:
    two = mass[g] +0
    g = g + 3
    #print(two)
    out.append(two)
while k <= len(mass)-1:
    tree = mass[k] +0
    k = k + 3
    #print(tree)
    out.append(tree)
print(out)
