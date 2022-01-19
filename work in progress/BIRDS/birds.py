import turtle as bird
import random 
import time 


bird.speed(0)


bird.shape("triangle")

                                                                         
while True: 
    bird.goto(random.randint(-400, 400), random.randint(-400, 400))
    time.sleep(0.5)