import turtle 
import random

steven = turtle.Turtle()

steven.shape("turtle")
steven.penup()
steven.speed(0)
steven.left(90)

#draw three corners dots
steven.goto(0, 150)
steven.dot()
steven.goto(-180, -150)
steven.dot()
steven.goto(180, -150)
steven.dot()
steven.goto(0, 0)

#variables
x = 0
y = 0
counter = 0

while counter < 100000000:
    random_corner = random.randint(1, 3)
    if random_corner == 1:
        x = (x+0)/2
        y = (y+150)/2
        steven.color("red")
    if random_corner == 2:
        x = (x-180)/2
        y = (y-150)/2
        steven.color("blue")
    if random_corner == 3:
        x = (x+180)/2
        y = (y-150)/2
        steven.color("purple")

        
    steven.goto(x, y)
    steven.dot()
    counter += 1


wn = turtle.Screen()
wn.mainloop()