import turtle
import math

t = turtle
t.shape('circle')

x = 0
y = 0
V = 50
ay = 10
n = 1


def fall():

    x += V*dt
    y += W*dt + ay*dt**2/2
    W += ay*dt
    t.goto(x, y)


while n < 10:

    fall()
    n += 1
    if n >= 10:
        break

