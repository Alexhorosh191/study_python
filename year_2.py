def is_year_leap(arg):
    if arg % 4 == 0 and arg % 400 == 0 and arg % 100 != 0:
        return True
    else:
        False


print(is_year_leap(11))
