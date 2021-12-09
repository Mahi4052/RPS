from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = "Yes"
while player == "Yes":
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    print("If u want to continue the game then enter:(NO) else enter:(Yes)")
    player=input()
    if(player=="Yes"):
        pass
    else:
        print("You have ended the game")
        break
    computer = t[randint(0,2)]


