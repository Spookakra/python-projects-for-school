#WAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUP
#WAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUP
#WAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUP
#WAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUP
#WAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUP
#WAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUPWAKEUP
#(i put 5 because i like that number)
import random 

user_unrealistic_achievements = 0
computer_rightful_victories = 0
       
the_opps = ["rock", "paper", "scissors"]#😼
      # ^---------------------------------^ it go there
while True:
    user_input = input("type Rock/Paper/Scissors or 'Q' to quit").lower() 
    if user_input == "q":
        print("A wise choice, but most cowards were smart")
        break
    
    #when the
    if user_input not in the_opps:#😼
           
        continue
    random_number = random.randint(0, 2)
    #dawane: 0, Thin tree minecraft reference: 1, rango https://ih1.redbubble.net/image.955708145.6875/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg: 2
    computer_pickupgame = the_opps[random_number]
    #its the computers choice 
    print("The machine has spoken, it chooses", computer_pickupgame + ".")

    #The last half of "the world turned upside down" belongs here
    if user_input == "rock" and computer_pickupgame == "scissors":
        print("Do you feel happy with your win. The news say he was multilated beyond the point of recognition")
        user_unrealistic_achievements += 1
        continue

    elif user_input == "paper" and computer_pickupgame == "rock":
        print("You won through a flawed system of injustice, ROCK DOESN'T BEAT PAPER ON ANY OTHER PLANET")
        user_unrealistic_achievements += 1
        continue

    elif user_input == "scissors" and computer_pickupgame == "paper":
        print("Is this school appropriate? He got chopped to peices")
        user_unrealistic_achievements += 1
        continue
    
    #and now you're losing
    else:
        print("You lost the game and in turn the kids went with their mother")
        computer_rightful_victories += 1

print("You won", user_unrealistic_achievements, "times")
print("The computer won", computer_rightful_victories, "times")

if computer_rightful_victories > user_unrealistic_achievements:
    print("The machine has won the match")
    print("but you should have expected that")
    print("You will never see your skin, wife, kids or the light of day ever again")
else:
    print("You won the match")
    print("BUT, it's bitter sweet cause you didn't win the court case")




#if you do like + instead of a comma is a print thing it will not do the space (very cool)
#a dumb cod quote was here so i could use it but i decided against it (very dumb)
#if you read this can you make a comment in the canvas assignment if you've seen 'arcane' and if so what your opinions on it are
#reminder to chill on the skin thing and become more original or sum
#do you use vscode and use 'the doki theme' and dont like the color scheme for astolfo but want to use the wallpaper with matching colors? I would recomend using the 'misato
# ' color scheme
