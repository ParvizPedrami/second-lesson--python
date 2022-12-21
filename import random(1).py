import random

pc_number = random.randint(0,20)
guess=0
while true :
    user_number=int(input("please enter your number"))
    if pc_number == user_number:
        print("you win")
        guess= guess+1
        print("your guess number", guess)
        break
    if pc_number > user_number:
        print("too high")
    else:
        print("too low")

input("press E to exit")
if input== E:
    exit
