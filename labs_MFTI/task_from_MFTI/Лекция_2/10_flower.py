import turtle


def draw_flower():
    turtle.shape('turtle')
    step = 25

    def draw_two_circle():
        turn = 10
        number_of_turns = 360 // turn
        for i in range(number_of_turns * 2):
            if i < number_of_turns:
                turtle.forward(step)
                turtle.left(turn)
            if i >= number_of_turns:
                turtle.forward(step)
                turtle.right(turn)

    draw_two_circle()
    turtle.forward(step / 2)
    turtle.left(45)
    draw_two_circle()
    turtle.left(90)
    draw_two_circle()


draw_flower()
