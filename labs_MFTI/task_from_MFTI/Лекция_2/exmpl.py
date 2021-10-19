import turtle

t = turtle
n = 5
d = 100


def star(t, n, d):
    angle = (180 - ((180 * (n - 2)) / n)) * 2
    for i in range(n):
        t.forward(d)
        t.left(angle)
    return angle


star(turtle, n, d)
