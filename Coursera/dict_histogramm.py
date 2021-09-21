names = open(input('Enter name of file:'))
counts = dict()
for name in names:
    if name.startswith('From:'):
        words = name.split()
        for word in words:
            if word is words[1]:
                counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count


print(bigword, bigcount)