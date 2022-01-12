import turtle as player 
import time


wn = player.Screen()
wn.title("disney level animation")
wn.bgcolor("Black")


player_sprite ="Intro to pygame\Animation\Unknown\no_anim_0.gif"
wn.addshape(player_sprite)
player.color("White")

def player_animate():
    player.shape("square")
    time.sleep(0.5)
    player.shape("circle")
    time.sleep(0.5)


while True:
    player_animate()









wn.mainloop()


