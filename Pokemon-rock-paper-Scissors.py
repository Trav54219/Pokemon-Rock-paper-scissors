import random 
import re
import os

winning_messages = ()
losing_messages1 = ("Charmander beats Bulbasaur, I win! ", "You lose!")
losing_messages2 = ("Bulbasaur beats Squirtle! I win! ", "You lose!")
losing_messages3 = ("Squirtle beat Charmander, I win! ", "You lose!")

os.system('cls' if os.name=='nt' else 'clear')
while 1< 2:
    print("\n")
    print("Charmander, Squirtle, Bulbasaur- Shoot!")
    userChoice = input("Choose your pokemon [C]harmander], [S]quirtle, or [B]ulbasaur: ")
    if not re.match("[CcSsBb]", userChoice):
        print("Please choose a pokemon:")
        print("[C]harmander], [S]quirtle, or [B]ulbasaur.")
        continue
    # Echo the user's choice
    print("You chose:", userChoice)
    choices = ['C', 'S', 'B']
    opponentChoice = random.choice(choices)
    print("I chose:", opponentChoice)
    
    
    if opponentChoice == str.upper(userChoice):
        print("Tie! ")
    #if opponenetChoice == str("C") and str.upper(userChoice) == "S"
    elif opponentChoice == 'C' and userChoice.upper() == 'B':      
        print(random.choice(losing_messages1))
        continue
    elif opponentChoice == 'B' and userChoice.upper() == 'S':      
        print(random.choice(losing_messages2))
        continue
    elif opponentChoice == 'S' and userChoice.upper() == 'C':
        print(random.choice(losing_messages3))
        continue
    else:       
        print("You win!")





