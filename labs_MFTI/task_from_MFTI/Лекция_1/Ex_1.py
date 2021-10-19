import numpy as np


def solving_the_equation():
    x = float(input('Введите число... '))
    z = float(1 / (np.e ** np.sin(x) + 1))
    n = float(5 / 4 + 1 / x ** 1 * 5)
    y = float(np.log(z / n) / np.log(1 + x ** 2))
    print('Ответ = ', y)


solving_the_equation()
