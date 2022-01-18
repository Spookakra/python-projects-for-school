import turtle as player 



wn = player.Screen()
wn.title("disney level animation")
wn.bgcolor("Black")

#create new shapes
wn.register_shape("invader.gif")
wn.register_shape("invader2.gif")


player.shape("invader.gif")
player.frame = 0

def player_animate():
  if player.frame == 0:
    player.shape("invader2.gif")
    player.frame = 1
    player.shape("invader2.gif")
  elif player.frame == 1:
    player.shape("invader.gif")
    player.frame = 0
  
  #TIMER STARTO 
  wn.ontimer(player_animate, 500)

player_animate()

while True:
  wn.update()
  print("space")
  print("vaidable")









wn.mainloop()