import turtle


def butterfly():

    turtle.shape('turtle')
    turtle.right(90)
    diameter = 50
    number_of_circle = 1
    while number_of_circle <= 10:
        turtle.circle(diameter)
        turtle.circle(-diameter)
        diameter += 10
        number_of_circle += 1


butterfly()
