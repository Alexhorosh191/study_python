import turtle


def draw_ten_quadrates():
    turtle.shape('turtle')
    numder_of_offset = 10
    offset = -25
    side_length = 50

    def draw_quadrate():
        number_of_sides = 4
        while number_of_sides > 0:
            turtle.forward(side_length)
            turtle.left(90)
            number_of_sides -= 1

    while numder_of_offset > 0:
        draw_quadrate()
        turtle.penup()
        turtle.goto(offset, offset)
        turtle.pendown()
        side_length += 50
        offset += -25
        numder_of_offset -= 1


draw_ten_quadrates()
