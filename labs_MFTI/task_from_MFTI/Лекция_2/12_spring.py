import turtle


def draw_spring():

    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(-350, -0)
    turtle.pendown()
    turtle.left(90)
    spring_diameter = 50
    coil_diameter = 10
    spring_coil = 1
    while spring_coil <= 8:
        turtle.circle(-spring_diameter, 180)
        turtle.circle(-coil_diameter, 180)
        spring_coil += 1


draw_spring()
