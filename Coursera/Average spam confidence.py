fname = input("Enter file name: ")
fh = open(fname)
count = 0
summa = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        x = line.find('0')
        y = line[x:]
        number = float(y)
        summa += number
midnumber = summa / count
print("Average spam confidence:", midnumber)

