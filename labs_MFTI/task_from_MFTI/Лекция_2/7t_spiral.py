import turtle
from numpy import pi


def draw_spiral():
    turtle.shape("turtle")
    spiral_step = 0
    while spiral_step < 15:
        turtle.forward(spiral_step / 2 * pi)
        turtle.left(2 * pi)
        spiral_step += 0.03


draw_spiral()

