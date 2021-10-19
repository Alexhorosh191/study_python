import turtle


def draw_spider():
    turtle.shape("turtle")
    number_of_paw = 12
    angle = 360 / 12
    while number_of_paw > 0:
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)
        turtle.left(angle)
        number_of_paw -= 1


draw_spider()
