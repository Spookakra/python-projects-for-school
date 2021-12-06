#Dice Roll Simulator 
import random

options = ["y", "n"]
dice_roll = random.randint(1,6)

while True:
    mans_question = input("Do you want to roll a dice litte child (y/n)")
    if mans_question == "y":
        print("commence the dice roll")
        print("you rolled a", dice_roll)
        break
    elif mans_question == "n":
        print("ok then")
        quit()
    if mans_question not in options:
        print("that's not an answer")
        continue

while True:
    rollin = input("would you like to roll again? (y/n)")
    if rollin == "y":
        print("nice")
        print("you rolled a", dice_roll)
        continue
    elif rollin == "n":
        print(":sadge:")
        quit()
    if rollin not in options:
        print("that's not an answer")
        continue

    