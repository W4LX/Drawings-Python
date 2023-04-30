from turtle import *
import random
import math

setup(900, 500)
bgcolor("black")

a1 = Turtle()
b1 = Turtle()
c1 = Turtle()
d1 = Turtle()
e1 = Turtle()

a1.color('cyan')
b1.color('red')
c1.color('purple')
d1.color('yellow')
e1.color('red')

turtlist = []
turtlist.append(a1)
turtlist.append(b1)
turtlist.append(c1)
turtlist.append(d1)
turtlist.append(e1)

speed(0)
tracer(0)
hideturtle()

sum = 0
count = 0

for j in range(100):
    for i in range(10000):
        for turt in turtlist:
            turt.seth(random.randrange(0, 360, 90))
            turt.fd(10)
        update()
    for turt in turtlist:
        sum += math.sqrt(turt.xcor()*turt.xcor() + turt.ycor()*turt.ycor())/10 * \
            2*math.sqrt(turt.xcor()*turt.xcor() +
                        turt.ycor()*turt.ycor())/10*2/100
        count += 1
    for turt in turtlist:
        turt.clear()
        turt.up()
        turt.goto(0, 0)
        turt.down()
    # print(sum/count)
