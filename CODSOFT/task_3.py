                                                    #Task3: ROCK-PAPER-SCISSORS GAME
print("         WELCOME TO THE GAME       ")
print("        ---------------------        ")
print("INSTRUCTIONS: \n1. Rock beats Scissors. \n2. Scissors beat Paper. \n3. Paper beats Rock.")
import random
user_choice=int(input(" Type 0 for ROCK \n Type 1 for PAPER \n Type 2 for SCISSORS \n Enter your choice : "))
if user_choice>=3 or user_choice<0:
    print("Please enter a valid number(0,1,2) and try again!!")
else:
    computer_choice=random.randint(0,2)
    print("Computer choice : ",computer_choice)
    if computer_choice==user_choice:
        print("It's a tie!!")
    elif computer_choice==0 and user_choice==2:
        print("Oh! You lose")
    elif user_choice==0 and computer_choice==2:
        print("You won!!!")
    elif computer_choice<user_choice:
        print("You won!!!")
    elif computer_choice>user_choice:
        print("Oh! You lose")
    