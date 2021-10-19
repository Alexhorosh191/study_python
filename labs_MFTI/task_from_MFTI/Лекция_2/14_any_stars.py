import turtle


def draw_any_stars():
    turtle.shape('turtle')
    number_of_top = 11  # number_of_top = n
    star_side = 100
    m = 5  # m-th circle = m
    """Each vertex of a regular n-polygon is connected to the
    m-th from it on a circle clockwise.
    The star obtained in this way is denoted as {n/m}.
    Now this function draws star like {11/5}"""
    angle = (180 - ((180 * (number_of_top - 2)) / number_of_top)) * m
    turtle.left(180 - angle)
    for i in range(number_of_top):
        turtle.forward(star_side)
        turtle.left(angle)
    return angle


draw_any_stars()



