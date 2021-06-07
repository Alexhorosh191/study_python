def square(arg):
    P = arg * arg
    S = arg * 4
    D = arg * 2**0.5
    return [P, S, D]


print(square(5))
