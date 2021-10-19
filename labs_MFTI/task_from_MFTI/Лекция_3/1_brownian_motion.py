import turtle
from random import randint


def draw_brownian_motion():
    turtle.shape('turtle')
    random_number = randint(0, 100)
    i = 1  # variable to end the loop

    def random_left_turn():
        random_step = randint(10, 100)
        random_turn = randint(0, 360)

        turtle.forward(random_step)
        turtle.left(random_turn)

    def random_right_turn():
        random_step = randint(10, 100)
        random_turn = randint(0, 360)

        turtle.forward(random_step)
        turtle.left(random_turn)

    while random_number < 50:
        random_left_turn()
        i += 1
        if random_number > 50:
            random_right_turn()
            i += 1
            continue
        if i > 200:
            break


draw_brownian_motion()

"""Doesn't work very well. FIXME"""
