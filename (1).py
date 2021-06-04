

"""def arithmetic(arg1, arg2, op):
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


print(arithmetic(2, 2, '+'))"""

"""def is_year_leap(arg):
    if arg % 4 == 0:
        return True
    else:
        False

print(is_year_leap(11))"""

"""def square(arg):
    P = arg * arg
    S = arg * 4
    D = arg * 2**0.5
    return [P, S, D]

print(square(5))"""

"""def season(arg):
    if arg in [12, 1, 2]:
        return 'winter'
    elif arg in [3, 4, 5]:
        return 'spring'
    elif arg in [6, 7, 8]:
        return 'summer'
    elif arg in [9, 10, 11]:
        return 'autumn'
    else:
        return False

print(season(1022))"""


"""def bank(rub, years):

    summa = rub * (1 + 0.1) ** years
    return summa

print(bank(1000, 2))"""


"""def bank(a, years):

    for year in range(years):
        a *= 1.1
    return a

print(bank(1000, 3))"""  # это очень интересный пример range


"""def is_prime(number):
    if number == 1:
        return False  # 1 - не простое число

    for p in range(2, number):
        if number % p == 0:
            return False

    else:
        return True

print(is_prime(1))"""  # я туп и не допер сам


check_number_higher_year = 1  # это высокосный год
check_february = 28  # 1 это високосный год

check_month = 1  # 1 это правда
check_day = 1  # 1 это правда
check_year = 1  # 1 это правда

true_numbers = (check_month, check_day, check_year)


def date(day, month, year):
    global check_year
    if year < 1:
        check_year = 0
    if day > 31:
        check_day = 0
    elif day < 1:
        check_day = 0

    def check_month():
        global check_month
        if month in range(1, 13):
            check_month = 1
        else:
            check_month = 0

    def check_year():
        global check_number_higher_year
        global check_february
        if year % 4 == 0:
            check_number_higher_year = 1
        if check_number_higher_year == 1:
            check_february = 29

    def check_days():
        global check_day
        global check_february
        numbers_31 = [1, 3, 5, 7, 8, 10, 12]
        number_30 = [4, 6, 9, 11]
        if month in numbers_31:
            check_day = 1
        elif month in number_30:
            check_day = 1
        elif month == 2:
            check_day = 1
        else:
            check_day = 0

    check_month()
    check_year()
    check_days()


    if true_numbers[0] == 0:
        print(False)
    elif true_numbers[1] == 0:
        print(False)
    elif true_numbers[2] == 0:
        print(False)
    else:
        print(True)

date(5555, 14, 2000)




"""def month(month):
    numbers_31 = [1, 3, 5, 7, 8, 10, 12]
    number_30 = [4, 6, 9, 11]
    if month in numbers_31:
        day = 31
    elif month in number_30:
        day = 30
    elif month == 2:
        day = 28
    else:
        day = False
    print(day)

month(2)"""




