def is_prime(number):
    if number == 1:
        return False  # 1 - не простое число

    for p in range(2, number):
        if number % p == 0:
            return False

    else:
        return True


print(is_prime(1))
