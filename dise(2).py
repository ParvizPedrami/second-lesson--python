import random

dise= random.randint(1,6)
prize= random.randint(1,6)

while dise <= 6:
    if dise <6:
        print("dise shows a number:", dise)
        break
    else:
        print("dise shows a number", dise)
        print("so programm throw the dise two more times:\n first throw: ", prize,"\n second throw: ",prize)
        break
