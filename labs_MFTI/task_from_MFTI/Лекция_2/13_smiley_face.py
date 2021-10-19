import turtle


def draw_smiley_face():

    turtle.shape('turtle')

    def draw_face():
        turtle.penup()
        turtle.goto(0, -200)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(200)
        turtle.fillcolor("yellow")
        turtle.end_fill()

    def draw_left_eye():
        turtle.penup()
        turtle.goto(-80, 80)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.fillcolor("blue")
        turtle.end_fill()

    def draw_right_eye():
        turtle.penup()
        turtle.goto(80, 80)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(25)
        turtle.fillcolor("blue")
        turtle.end_fill()

    def draw_nose():
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.pensize(10)
        turtle.right(90)
        turtle.forward(70)

    def draw_smile():
        turtle.penup()
        turtle.goto(-100, -80)
        turtle.pendown()
        turtle.color("red")
        turtle.circle(100, 180)

    draw_face()
    draw_left_eye()
    draw_right_eye()
    draw_nose()
    draw_smile()


draw_smiley_face()
