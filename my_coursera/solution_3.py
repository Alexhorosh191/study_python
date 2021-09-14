import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

discriminant = b ** 2 - 4 * a * c


if discriminant == 0:
    x_1 = x_2 = -b / (2 * a)
    x_1 = int(x_1)
    x_2 = int(x_2)
    print(x_1, "\n", x_2)
elif discriminant > 0:
    x_1 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x_2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x_1 = int(x_1)
    x_2 = int(x_2)
    print(x_1, "\n", x_2)
