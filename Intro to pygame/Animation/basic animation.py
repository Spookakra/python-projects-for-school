import turtle as player 
import time


wn = player.Screen()
wn.title("disney level animation")
wn.bgcolor("Black")

player.shape("sqaure")
player.color("White")

def player_animate():
    player.shape("square")
    time.sleep(0.5)
    player.shape("circle")
    time.sleep(0.5)


while True:
    player_animate()









wn.mainloop()


