from turtle import *
from colorsys import *

bgcolor("black")
speed(0.5)

r = 60
x = 0

for i in range(360):
    c = hsv_to_rgb(x, 1, 0.85)
    x += 1 / r

    color(c)
    left(1)
    fd(1)

    for i in range(2):
        left(2)
        circle(100)
