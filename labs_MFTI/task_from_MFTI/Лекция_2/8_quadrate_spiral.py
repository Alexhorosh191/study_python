import turtle


def draw_quadrate_spiral():
    turtle.shape("turtle")
    spiral_step = 10
    while spiral_step < 200:
        turtle.forward(spiral_step)
        turtle.left(90)
        turtle.forward(spiral_step)
        turtle.left(90)
        spiral_step += 10


draw_quadrate_spiral()
