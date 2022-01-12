import turtle as player 
import time


wn = player.Screen()
wn.title("disney level animation")
wn.bgcolor("Black")


player.shape("square")
player.color("White")

while True:
    player.shape("square")
    time.sleep(0.5)
    player.shape("circle")
    time.sleep(0.5)











wn.mainloop()


