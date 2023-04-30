from turtle import *

bgcolor("black")
speed(0)

radius = 60
pensize(2)

colours = ["orange", "pink", "yellow"]

for x in range(12):
    color(colours[x % 3])

    for i in range(6):
        circle(radius)
        right(60)

    radius = radius + 4

hideturtle()
mainloop()
