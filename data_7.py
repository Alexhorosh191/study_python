check_february = 28
check_month = 1  # 1 это правда
check_day = 1  # 1 это правда
check_year = 1  # 1 это правда


def date(day, month, year):
    global check_year
    global check_month
    global check_day
    if year < 1:
        check_year = 0

    def check_months():
        global check_month
        if month in range(1, 13):
            check_month = 1
        else:
            check_month = 0

    def check_years():
        global check_february
        if year % 4 == 0:
            check_number_higher_year = 1
        else:
            check_number_higher_year = 0
        if check_number_higher_year == 1:
            check_february = 29

    def check_days():
        global check_day
        global check_february
        numbers_31 = [1, 3, 5, 7, 8, 10, 12]
        number_30 = [4, 6, 9, 11]
        if month in numbers_31:
            if 1 <= day <= 31:
                check_day = 1
            else:
                check_day = 0
        elif month in number_30:
            if 1 <= day <= 30:
                check_day = 1
            else:
                check_day = 0
        elif month == 2:
            if 1 <= day <= check_february:
                check_day = 1
            else:
                check_day = 0
    check_months()
    check_years()
    check_days()

    true_numbers = (check_month, check_day, check_year)
    if true_numbers[0] == 0:
        print(False)
    elif true_numbers[1] == 0:
        print(False)
    elif true_numbers[2] == 0:
        print(False)
    else:
        print(True)


date(29, 2, 2021)
