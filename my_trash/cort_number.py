fuck = [2, 5, 90, 120, 335, 3, 4]
print(fuck)
x = len(fuck)

count = 0
for y in range(x-1):
    for i in range(x-1):
        if fuck[i] > fuck[i+1]:
            count += 1
            fuck[i], fuck[i+1] = fuck[i+1], fuck[i]

print(count)
print(fuck)