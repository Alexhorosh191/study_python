import turtle


def draw_index():
    turtle.shape("turtle")
    turtle.pencolor("blue")
    turtle.fillcolor("blue")
    turtle.pensize(5)
    a = 50  # drawing line length
    d = 70  # diagonal drawing line length
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()

    def draw_zero():
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a * 2)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a * 2)
        turtle.penup()
        turtle.right(90)
        turtle.forward(a * 2)
        turtle.pendown()

    def draw_one():
        turtle.penup()
        turtle.right(90)
        turtle.forward(a)
        turtle.pendown()
        turtle.left(135)
        turtle.forward(d)
        turtle.right(135)
        turtle.forward(a * 2)
        turtle.right(180)
        turtle.forward(a * 2)
        turtle.right(90)
        turtle.penup()
        turtle.forward(a)
        turtle.pendown()

    def draw_four():
        turtle.right(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(180)
        turtle.forward(a * 2)
        turtle.right(90)
        turtle.penup()
        turtle.forward(a)
        turtle.pendown()

    def draw_seven():
        turtle.forward(a)
        turtle.right(135)
        turtle.forward(d)
        turtle.left(45)
        turtle.forward(a)
        turtle.penup()
        turtle.right(180)
        turtle.forward(a * 2)
        turtle.right(90)
        turtle.forward(a * 2)
        turtle.pendown()

    index = (draw_one(), draw_four(), draw_one(),
             draw_seven(), draw_zero(), draw_zero())


draw_index()
