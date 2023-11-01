#blackjack
import random 



first_card = random.randint(1,11)

playerbet = input("how much would you like to bet? ")


while True:
    if playerbet.isdigit() == False:
        print("Not a valid number")  
        continue
    else:
        break

playerbet = int(playerbet)

while True:
    if playerbet >= 0:
        break
    else:
        print("Number Invalid")
        continue

val = 0

#def main():
#    skip

while val < 22: 
    if val == 21:
        break
    elif input(): 



quit()