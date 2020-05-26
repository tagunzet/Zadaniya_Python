
mass = []
data = []
with open("input") as f:
    for line in f:
        data.append([float(x) for x in line.split()])


h = open('output', 'w')

print(data)
print(data[0])
print(data[1])
resultpapka = [int(item) for item in data[0]]
print(resultpapka)

synok1 = ''
synok2 = ''

papka= resultpapka[0]

i = 0

massivchik_good_znacheniy = []

mag3 = []
result = [int(item) for item in data[1]]
print(result)
#print(result[0]) // первый элемент массива чисел
a = len(result)
print(a)
while i in range(a):

    #print(i)
    #i = i + 1
    #print(i)
    #for x in result:
    if result[0] + result[i] == papka:

            print(result[0] , result[i], papka)
            print("krasava epta")
            massivchik_good_znacheniy.append(result[0])
            massivchik_good_znacheniy.append(result[i])
            massivchik_good_znacheniy.append(papka)

            h = open('output', 'w')
            h.write("1")

    elif result[i+1] + result[i] == papka:

        print(result[i-1], result[i], papka)
        mm = open('output', 'w')
        mm.write("1")


    else :

            print("no")
            print(result[0] ,  result[i], papka)

            massik = [0,0,0,0]
            #h.write("0")
            g = open('output', 'w')
            g.write("0")
            g.close()
            #


    i = i + 1

#запись в файл
#f.write(index + '\n')
print("Найдены два числа ")
print(massivchik_good_znacheniy)

#запись в файл
#a = open('output', 'w')
#a.write("1")

#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#sm = sum(a[0:len(a)]) # Sum of 'a' from 0 index to 9 index. sum(a) == sum(a[0:len(a)]
#print(sm)