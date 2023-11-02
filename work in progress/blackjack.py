#blackjack
import random 

suites = ["spades", "hearts", "diamonds", "clubs"]
values = ["Jack", "Queen", "King", 1 , 2 , 3, 4, 5, 6, 7, 8, 9]
usedcards = []

first_card = random.randint(1,9)

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

while True:
    answer = input("would you like to 'hit' or 'stand' ? ").lower() 
    if answer == 'hit':
        pass
    elif answer == 'stand':
        break 
    else:
        print("Not a valid")
        





quit()
