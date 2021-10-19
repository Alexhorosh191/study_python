import turtle
from math import sin, pi


def draw_ten_polygons():
    turtle.shape('turtle')
    polygon_offset = 30
    number_of_top = 3
    turtle.up()
    turtle.goto(polygon_offset, 0)
    turtle.down()

    def polygon():
        first_top = 0
        while first_top < number_of_top:
            turtle.left(((180 - 360 / number_of_top) / 2) + (360 / number_of_top))
            turtle.forward(2 * polygon_offset * sin(pi / number_of_top))
            first_top += 1
            turtle.right((180 - 360 / number_of_top) / 2)

    while number_of_top < 13:
        polygon()
        number_of_top += 1
        polygon_offset += 20
        turtle.up()
        turtle.goto(polygon_offset, 0)
        turtle.down()


draw_ten_polygons()
