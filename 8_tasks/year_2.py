def is_year_leap(arg):
    if arg % 400 == 0:
        return True
    if arg % 4 == 0 and arg % 100 != 0:
        return True

    return False


print(is_year_leap(1900))
