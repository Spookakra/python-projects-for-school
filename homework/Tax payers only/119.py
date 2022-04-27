#pattern genarater
import random as grn
import turtle as trtl

wn = trtl.Screen()
ninja = trtl.Turtle()
t = trtl.Pen()

pattern = grn.randint(1, 3)

if pattern == "1":   
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    trtl.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x//100 + 1)
        t.forward(x)
        t.left(59)


elif pattern == "2":

    trtl.speed(2)

    for i in range(100):
        trtl.circle(5*i)
        trtl.circle(-5*i)
        trtl.left(i)

else:

    ninja.speed(10)


    for i in range(180):
        ninja.color("red")
        ninja.forward(100)
        ninja.right(30)
        ninja.color("blue")
        ninja.forward(20)
        ninja.left(60)
        ninja.color("green")
        ninja.forward(50)
        ninja.right(30)

        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()

        ninja.right(2)





