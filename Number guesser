import random
from operator import truediv

secret=random.randint(1,100)
attempts=0
won=False

while attempts<5 and won==False:
    guess=int(input("Guess a number between 1 and 100: "))

    if guess<1 or guess>100:
        print("Invalid number")
    elif guess>secret:
        print("Too high")
        attempts+=1
    elif guess<secret:
        print("Too low")
        attempts+=1
    else: #guess=secret
        won=True
if won:
    print("Congratulations! You won!"+str(attempts))
    if attempts==1:
        print("Rating:Genius")
    elif attempts<=3:
        print("Rating:Great")
    else:
        print("Rating: Good")
else:
    print("Sorry, you lost")
