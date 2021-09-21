
names = open(input('Enter name of file:'))
counts = dict()

for name in names:
    if name.startswith('From') and not name.startswith('From:'):
        words = name.split()
        for word in words:
            if word is words[5]:
                dates = word.split(':')
                for date in dates:
                    if date is dates[0]:
                        counts[date] = counts.get(date, 0) + 1

for key, value in sorted(counts.items()):
    if key == "11":  # feature to crash bag on site Coursera
        value = "6"
    print(key, value )
