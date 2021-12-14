#i am very sorry

import random
import socket
import time



your_location = socket.gethostbyname('eda.gay')


top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 🥺")
        quit()

else:
    print("Please type a number idiotic child") 
    quit()



random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    users_dumb_guess = input("GUESS rn: ")

    if users_dumb_guess.isdigit():
       users_dumb_guess = int(users_dumb_guess)
    else:
        print("Please type a number idiotic dumb stupid useless child")
        continue
    
    if users_dumb_guess == random_number:
        print("CONGRATS, You get to keep your skin")
        break
    else:
        print(your_location, "Im comming for you")

    if users_dumb_guess > random_number:
        print("Also, you're too high you dumb addict 🌞")
    else:
        print("Too low, elevate your thinking to the sigma grindset")


print("It really took you", guesses, "tries?")
print("blocked")
time.sleep(3)
quit


#nvm, not sorry
#im not cleaning it up its beautiful




