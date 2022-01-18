import turtle as player 



wn = player.Screen()
wn.title("disney level animation")
wn.bgcolor("Black")

#create new shapes
wn.register_shape("invader.gif")
wn.register_shape("invader2.gif")


player.shape("invader.gif")
player.frame = 0

#copying the video
player.frames = ["invader.gif", "invader2.gif"]   


def player_animate():
  player.frame += 1
  if player.frame >= len(player.frames):
    player.frame = 0
  player.shape(player.frames[player.frame])
   
  
  #TIMER STARTO 
  wn.ontimer(player_animate, 500)

player_animate()

while True:
  wn.update()
  print("space")
  print("vaidable")









wn.mainloop()