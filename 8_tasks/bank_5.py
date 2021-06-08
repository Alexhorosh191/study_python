def bank(rub, years):

    summa = rub * (1 + 0.1) ** years
    return summa


print(bank(1000, 2))
"""def bank(a, years):

    for year in range(years):
        a *= 1.1
    return a

print(bank(1000, 3))"""  # это очень интересный пример range
