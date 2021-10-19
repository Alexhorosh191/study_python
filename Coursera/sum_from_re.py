"""import re

open_file = open("text.txt", "r")
numbers = re.findall('[0-9]+', open_file.read())
result = [int(item) for item in numbers]
print(sum(result))"""



import re
print(sum([int(item) for item in re.findall('[0-9]+', open('text.txt').read())]))

