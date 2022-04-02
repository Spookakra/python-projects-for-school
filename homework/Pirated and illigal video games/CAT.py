# catch a turtle.py
#-----import statements-----
import turtle 
import os
import random as rand
import LeaderBoared as lb
import time

#-----name input-----
os.system('cls||clear')

while True:
  player_name = input("What are your initials? ").upper()
  if len(player_name) > 3:
    print("3 Chracters max")
    time.sleep(2)
    os.system('cls||clear')
    continue
  else:
    break

#-----game configuration----
wn = turtle.Screen()


score_writer = turtle.Turtle()
score_final = turtle.Turtle()
font_configuration = ("impact", 20, "normal")
font_final = ("impact", 20, "normal")  

nm835_color = "pink"
nm835_size = 2
nm835_shape = "triangle"
score = 0

leaderboard_filename = "LeaderBoared.txt"

#-----initialize turtle-----
wn.screensize(400, 500)
noobmaster835 = turtle.Turtle()
noobmaster835.shape(nm835_shape)
noobmaster835.color(nm835_color)
noobmaster835.turtlesize(nm835_size) 
noobmaster835.penup()
score_writer.hideturtle()
score_final.hideturtle()
score_writer.penup()
score_final.penup()
score_writer.goto(-300, 257)
score_final.goto(-55, 50)


#-----countdown variables-----
font_setup = ("Impact", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----countdown writer-----
counter =  turtle.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(230, 257)

#-----game functions--------

def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_filename)
  leader_scores_list = lb.get_scores(leaderboard_filename)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_filename, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

def countdown():
  global timer, timer_up, score
  counter.clear()
  if timer <= 0:
    counter.clear()
    counter.goto(-50, 80)
    counter.write("Time's Up", font=font_setup)
    score_final.write("Your final score was: " +  str(score))
    timer_up = True
    manage_leaderboard()

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def update_score():
    score_writer.clear()
    global score
    if timer > 0:
        score += 1
        score_writer.write(score, font=font_configuration)
    else:
        pass

def change_position():
    noobmaster835.goto(rand.randint(-300, 300), rand.randint(-300, 300))

def nm835_clicked (x, y):
    update_score()
    change_position()

#-----events----------------
noobmaster835.onclick(nm835_clicked)


wn.ontimer(countdown, counter_interval) 
wn.mainloop()