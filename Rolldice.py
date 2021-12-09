import random 
def rolldice(x):
    while x == "r":
        print("Dice rolling...............")
        print("----Random Value is Below----")
        no = random.randint(1,6)
        if no == 1: print("*")
        if no == 2: print("**")
        if no == 3:
            print("* *")
            print(" * ") 
        if no == 4: 
            print("**") 
            print("**") 
        if no == 5:
            print("* *") 
            print(" * ") 
            print("* *") 
        if no == 6: 
            print("***") 
            print("***") 
        print("enter r to roll dice again or else e for exit")
        x=input()
print("enter r to roll dice:",end=" ")
rolldice(input())

