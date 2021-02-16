import turtle
import math

def love():
    m=1
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    while True:
        r = 100 * (1 - math.sin((2 * math.pi / 360) * m))
        turtle.goto(r*math.cos((2 * math.pi / 360) * m),r*math.sin((2 * math.pi / 360) * m))
        m=1+m


love()
