import turtle as player 
import time


wn = player.Screen()
wn.title("disney level animation")
wn.bgcolor("Black")

player.color("White")

def player_animate():
  if player.shape() == "sqaure":
    player.shape("circle")
  elif player.shape() == "circle":
    player.shape("square")
  

    #TIMER STARTO 
    wn.ontimer(player_animate, 50)

player_animate()

while True:
  wn.update()
  print("fnaf")
  print("feddy")









wn.mainloop()