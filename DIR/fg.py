import itertools





with open('input.txt') as f:

        a,b = f.read().splitlines()

a = int(a)
b = map(int, b.split(' '))

comb = itertools.combinations(b, 2)

result = map(sum, comb)



with open('output.txt', 'w') as h:
    h.write("1" if a in result else "0")

