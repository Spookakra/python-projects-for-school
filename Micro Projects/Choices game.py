#text based adventure game (comming soon)
import random
import time

fightingchance = random.randint(1,6)

player_name = input("what is your name")

print("hello", player_name, "welcome to:")
print("TEXT BASED ADVENTURE GAME")
print("make your first choice:")

answer = input("You are on a dirt road, it has come to an end and you can go 'left' or 'right'.").lower()

if answer == "left":
    answer = input("You come across a traveling trader with tons of tightropes, you can 'fight' him or ask him if would you like to 'trade'")

    if answer == "fight":
            if fightingchance > 3:
                print("you land a punch!")
                print("he had a gun")

            else: 
                print("It is not a good idea to attempt to kill the first person you come across. You die a very painfull death")
    elif answer == "trade":
        print("You remember you dont have any money and while trying to find another object to trade with the man gets angry and murders you for inturupting his travels.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to 'cross' it or 'head back'")

    if answer == "back":
        print("You go back and fall into a pitfall!")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet the ending sequence? is it 'cool' or 'not'")

        if answer == "cool":
            print("wrong its a text based game idiot")
        elif answer == "not":
            print("yea uh ok")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option.')
    print('You shall suffer a fate worse than death:')
    print('ITS ABOUT LIES 🤞 ITS ABOUT VENTING 🕳 WE STAY SUSSY 😈 WE IMPOSTOR 📮 KILL IN O2 💨 KILL IN REACTOR 🔋 AND SABOTAGE 💥 I GOT IMPOSTOR IN MY VEINS 🫀 I NEED TO KILL THE CREWMATES 🔪 I WON THE GAME 🏆 SO WHATS MY MOTHERSUSSING NAME? 🗣 BAKA 😈📮')

print("Thank you for trying", player_name, "now get out")
time.sleep(3)
quit