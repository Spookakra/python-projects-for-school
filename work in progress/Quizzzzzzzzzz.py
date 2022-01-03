#I want to start this by saying im making this thing without watching the video at all
#I will be accepting medals for my smartness if you would like to submit one please dm 'Spookakra#5894' 
#I may be doing this the hard way but i dont care 
#Its best to minamize the loops idk if you can do that if you're using triket though (https://i.postimg.cc/ZR2wWBgR/likethis.png)
#this code is a WIP

import time

#corrrect choises 😩 (will probably remain at 0) 
tributes_to_the_almighty_linechu = 0
#truitious or fictitious
souldclod = ["true", "false"]
#the disposable end 
imgettingreallytires = ["1", "2", "3", "4"]


while True:
    Start_the_gammong = input("Would you like to take my quiz weary traveler (Hint you do not have a choice just type 'y')")
    if Start_the_gammong == "y":
        break
    else:
        continue
#first half 
#question 1 
while True: 
    first_question = input("'true' or 'false', League is a good and fun game") 
    if first_question == "false":
        print("you got it right")
        tributes_to_the_almighty_linechu += 1
        break
    elif first_question == "true":
        print("mori will never notice you at this pace")
        tributes_to_the_almighty_linechu =- 1
        break   
    
    if first_question not in souldclod:
        print("Thats not even and option")
        print("Its only 2 options try harder")
        continue
#question 2
while True: 
    second_question = input("'true' or 'false', I am on the run from the police") 
    if second_question == "true":
        print("FOR SHAME THAT YOU THINK OF ME THAT WAY")
        tributes_to_the_almighty_linechu -= 1
        break
    elif second_question== "false":
        print("this is the right answer")
        tributes_to_the_almighty_linechu += 1
        break   
    
    if second_question not in souldclod:
        print("Thats not even and option")
        print("Its only 2 options try harder")
        continue
#second_half
#question 3

while True:    
    third_question = input("multiple choice, what is the funniest number", "1: 32", "2: 8", "3: 96", "4: 53") 
    if third_question == "1":
        print("you got it right")
        tributes_to_the_almighty_linechu += 1
        break

    elif third_question == "2":
        print("The answer was everything but 3")
        tributes_to_the_almighty_linechu += 1
        break 

    elif third_question == "3":
        print("do you have no shame? DO YOU HAVE NO SHAME?")
        tributes_to_the_almighty_linechu -= 1
        break 

    elif third_question == "4":
        print("good job on being a cool person")
        tributes_to_the_almighty_linechu += 1
        break 

    else:
        print("Thats not even and option")
        print("Its only 4 options try harder")
        continue

#question 4
while True:    
    fourth_question = input("multiple How many elements are there on the periodic table?", "1: 112", "2: 120", "3: 118", "4: 153") 
    if fourth_question == "1":
        print("you've already been blocked by eden and your ip has been banned for his website")
        tributes_to_the_almighty_linechu -= 1
        break

    elif fourth_question == "2":
        print("just not right")
        tributes_to_the_almighty_linechu -= 1
        break 

    elif fourth_question == "3":
        print("This is The good ending")
        tributes_to_the_almighty_linechu += 1
        break 

    elif fourth_question == "4":
        print("*phantom forces lose screen*")
        tributes_to_the_almighty_linechu -= 1
        break 

    else:
        print("Thats not even and option")
        print("Its only 4 options try harder")
        continue

        
        
print("Your final score is", tributes_to_the_almighty_linechu)

#deciding your worth
if tributes_to_the_almighty_linechu < 0:
    print("I really hope you were trying to fail")
    print("How you get a negative score otherwise?")
    time.sleep(3)
    quit()

else:
    print("Congrats you beat the bear minimum")
    print("At least you're not a League player")
    print("(hopefully)")
    time.sleep(3)
    quit()




#i should have made this earlier im really tired 
#it was going to be 10 questions but i passed on that offer 





