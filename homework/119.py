#animal generator 
import turtle as bug
import time 


while True:
    print("choose a creature")
    grievances = input("1: Ladybug, 2: Spider, 3: Prog god, q: quit ")
    if grievances == "1":

        # create ladybug head
        ladybug = bug.Turtle()
        ladybug.pensize(40)
        ladybug.circle(5)
        ladybug.speed(0)

        # and body
        ladybug.penup()
        ladybug.goto(0, -55) 
        ladybug.color("red")
        ladybug.pendown()
        ladybug.pensize(40)
        ladybug.circle(20)
        ladybug.setheading(270)
        ladybug.color("black")
        ladybug.penup()
        ladybug.goto(0, 5)
        ladybug.pensize(2)
        ladybug.pendown()
        ladybug.forward(75)

        # config dots
        xpos = -20
        ypos = -55
        ladybug.pensize(10)

        # draw two sets of dots

        ladybug.penup()
        ladybug.goto(xpos, ypos)
        ladybug.pendown()
        ladybug.circle(4)
        ladybug.penup()
        ladybug.goto(xpos + 30, ypos + 20)
        ladybug.pendown()
        ladybug.circle(4)

        # position next dots
        ypos = ypos + 35
        xpos = xpos + 3
        ladybug.penup()

        #draw more dots
        ladybug.goto(xpos, ypos)
        ladybug.hideturtle()
        ladybug.pendown()
        ladybug.circle(4)

        # position more dots
        ypos = ypos + 16
        xpos = xpos + 25
        ladybug.penup() 

        #DOTS 
        ladybug.goto(xpos, ypos)
        ladybug.hideturtle()
        ladybug.pendown()
        ladybug.circle(4)

        time.sleep(3)
        bug.clearscreen()
        continue



    elif grievances == "2":
        pass

    elif grievances == "3":
        pass


    elif grievances == "q":
        break


    else:
        print("that's not an answer")
        continue


#i am stuck in a perpetual loop of pain
