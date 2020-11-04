import random

r = random.randint(1,49)
#print(r)

g=int(input("Enter a number between 1 and 49 : "))


while True:
    if g==r:
        print("You won")
        break
    elif g>r:
        print("Guess is high")
        g=int(input("Enter a number between 1 and 49 : "))

    elif g<r:
        print("Guess is low")
        g=int(input("Enter a number between 1 and 49 : "))

    else:
        print("invalid number")
        g=int(input("Enter a number between 1 and 49 : "))
