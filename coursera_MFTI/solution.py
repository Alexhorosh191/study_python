import sys

digit_string = sys.argv[1]

def print_summa(digit_string):
    x = 0
    for i in digit_string:
        i = int(i)
        x += i
    print(x)

print_summa(digit_string)
