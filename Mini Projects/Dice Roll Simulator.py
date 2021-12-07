#Dice Roll Simulator 
import random


first_dice_roll = random.randint(1,6)

while True:
    mans_question = input("Do you want to roll a dice litte child (y/n)")
    if mans_question == "y":
        print("commence the dice roll")
        print("you rolled a", first_dice_roll)
        break
    elif mans_question == "n":
        print("ok then")
        quit()
    else:
        print("that's not an answer")
        continue

while True:
    rollin = input("would you like to roll again? (y/n)")
    if rollin == "y":
        print("nice")
        print("you rolled a", random.randint(1,6))
        continue
    elif rollin == "n":
        print(":sadge:")
        break
    else:
        print("that's not an answer")
        continue

    