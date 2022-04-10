import turtle 

wn = turtle.Screen()
mazercise = turtle.Turtle()

mazercise.hideturtle()
mazercise.pensize(7)
mazercise.right(90)
mazercise.penup()
mazercise.goto(230, 240) 
mazercise.pendown()


WHOLES = 1
side = 450
turns = 0


while turns < 21:
    mazercise.forward(side)
    mazercise.right(90)
    side -= 20
    turns += 1



wn.mainloop()


