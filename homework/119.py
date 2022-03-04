import turtle
import time


wn = turtle.Screen()
wn.title("disney level animation")
wn.bgcolor("White")


bg_image = "homework\yeah.gif"
wn.addshape(bg_image)

def turtle_animate():
    turtle.shape("bg_image")


turtle_animate()

wn.mainloop()