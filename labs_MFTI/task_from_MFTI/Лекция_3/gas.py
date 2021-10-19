import turtle
from turtle import Screen, Turtle
from random import randint

x = randint(10, 20)
number_of_turtles = x
steps_of_time_number = 100
screen = Screen()
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.goto(randint(-200, 200), randint(-200, 200))


def move():





    unit.penup()
    n = randint(0, 100)
    i = 1 
    unit.speed(1)

    def rndl():
        x = randint(10, 100) 
        y = randint(0, 360)
 
        unit.forward(x)
        unit.left(y)
    

    def rndr():
        x = randint(10, 100) 
        y = randint(0, 360)

        unit.forward(x)
        unit.left(y)
    

    while n < 50:
        rndl()
        i += 1
        if n > 50:
            rndr()
            i += 1
            continue
        if i > 200:
            break




while True:
    for _ in range(steps_of_time_number):
        for units in pool:
            move()

"""
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:

    unit.penup()
    unit.speed(0)
    unit.goto(randint(-200, 200), randint(-200, 200))
    


for i in range(steps_of_time_number):   
    
    for unit in pool:   
        
        screen.delay(100)
        unit.goto(randint(-200, 200), randint(-200, 200))"""



"""for _ in range(steps_of_time_number):

    for units in pool:
       move()"""

