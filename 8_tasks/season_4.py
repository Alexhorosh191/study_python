def season(arg):
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


print(season(1022))
