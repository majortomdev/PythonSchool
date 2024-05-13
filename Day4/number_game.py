from random import randint

target = randint(1, 101)

tries = 8
while tries > 0:
    attempt = input("enter a number between 1 and 100:  ")
    if int(attempt) > target:
        tries -= 1
        print("Too high")
    elif int(attempt) < target:
        tries -= 1
        print("Too low")
    else:
        print("HURRAY You got it right")
        break
if tries==0:
    print("Sorry, you ran out of lives")