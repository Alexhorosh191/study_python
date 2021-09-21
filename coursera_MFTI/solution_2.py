import sys

digit_string = int(sys.argv[1])


def print_stairway(digit_string):

    for i in range(1, digit_string + 1):
        print(" " * (digit_string - i) + "#" * i)


print_stairway(digit_string)
