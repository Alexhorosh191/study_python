def arithmetic(arg1, arg2, op):
    if op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        return arg1 / arg2
    else:
        return "noname function"


print(arithmetic(2, 2, '+'))
