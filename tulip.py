import math
from turtle import *

bgcolor("black")
shape("turtle")
speed(0)
fillcolor("brown")

phi = 137.508 * (math.pi / 180.0)

for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()

    if i < 160:
        stamp()
    else:
        fillcolor("yellow")
        begin_fill()
        right(20)
        forward(70)
        left(40)
        forward(70)
        left(140)
        forward(70)
        left(40)
        forward(70)
        end_fill()

hideturtle()
mainloop()
