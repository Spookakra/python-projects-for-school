#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "homework\Activity 1.2.3\snapple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("homework\Activity 1.2.3\Background.gif")

apple = trtl.Turtle()

down = apple.ycor()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  

def down():
  global down
  down = down - 50


#-----function calls-----
draw_apple(apple)
down()

wn.mainloop()