import turtle

t = turtle
t.shape("turtle")
t.pencolor("blue")
t.fillcolor("blue")
t.pensize(5)
a = 50
d = 70
t.penup()
t.goto(-300, 0)
t.pendown()


inp = open('1.txt', "r") 
out = open('exmpl3.py', 'w')
s = inp.read()
out.write(s)
inp.close()
out.close()