

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
massiv = [a, b, c]


j = 1
massiv[0] = massiv[0] - massiv[j]
massiv.sort()
if a != massiv[1]:
    j = 2
    massiv[0] = massiv[0] - massiv[j]
    massiv.sort()
    print(massiv)
    if a != massiv[1]:
        print('NO')
else:
    print('YES')

j = 0
massiv[1] = massiv[1] - massiv[j]
massiv.sort()
if b != massiv[1]:
    j = 2
    massiv[1] = massiv[1] - massiv[j]
    massiv.sort()
    if b != massiv[1]:
        print('NO')
else:
    print('YES')


j = 0
massiv[2] = massiv[2] - massiv[j]
massiv.sort()
if c != massiv[1]:
    j = 1
    massiv[2] = massiv[2] - massiv[j]
    massiv.sort()
    if c != massiv[1]:
        print('NO')
else:
    print('YES')



