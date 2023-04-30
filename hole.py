from turtle import *

title("Agujero")
bgcolor("black")
pencolor("white")

speed(0)

x = 1
while x < 400:
    forward(5 + x)
    right(91)
    x += 1

hideturtle()
mainloop()
