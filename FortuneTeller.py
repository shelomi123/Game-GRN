import random

answer="y"

print("Welcome to the Fortune Teller Game")
print("You will select a color and a number and I will tell your future")

while answer == "y" :
    color= input("Enter a color from [red,blue,green,yellow]")

    if color=="red" or "green":
        number=int(input("Enter a number from [1,3,4,6]"))
        if number==1:
            print("You will have a car")
        elif number==3:
            print("You will have two kids")
        elif number==4:
            print("You will have a big house")
        elif number==6:
            print("You will be a doctor")
        else:
            print("Invalid number")

    elif color=="yellow" or "blue":
        number=int(input("Enter a number from [2,5,7,8]"))
        if number==2:
            print("You will have a car")
        elif number==5:
            print("You will have two kids")
        elif number==7:
            print("You will have a big house")
        elif number==8:
            print("You will be a doctor")
        else:
            print("Invalid number")
    
    else:
        print("Invalid color")
        answer=input('Press "y" to play and "n" to exit')
