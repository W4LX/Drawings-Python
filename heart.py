from turtle import *
from math import *

tracer(2)
bgcolor("black")
color("red")


def heartX(n):
    x = 15 * sin(n) ** 3
    return x


def heartY(n):
    y = 12 * cos(n) - 5 * cos(2 * n) - 2 * cos(3 * n) - cos(4 * n)
    return y


for i in range(800):
    goto(heartX(i) * 10, heartY(i) * 10)
    goto(0, 0)

exitonclick()
