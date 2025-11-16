import random
print ("WELCOME TO THE GAME")

def game():
    machine = random.randint(1,3)
    num= int(input("Enter \n1 : ROCK, 2 : PAPER, 3 : SCISSORS :"))
    if num == 1:
        "ROCK"
    elif num == 2:
        "PAPER"
    elif num == 3:
        "SCISSORS"
    if num == machine:
        print("It's a tie!")
    elif num==1 and machine==3 or num==2 and machine==1 or num==3 and machine==2:
        print("You win!")
    else:
        print("You lose!")
    
    choice= input("DO YOU WANT TO PLAY(yes/no)")
    if choice.lower() == "yes" or choice.lower() == "y":
        game()
    else:
        print("Thank you for playing!")

game()
