import random 
import re
import os

os.system('cls' if os.name=='nt' else 'clear')
while (1< 2):
    print("\n")
    print "Charmander, Squirtle, Bulbasaur- Shoot!"
    userChoice = raw_input("Choose your pokemon [C]harmander], [S]quirtle, or [B]ulbasaur: ")
    if not re.match("[CcSsBb]", userChoice):
        print "Please choose a pokemon:"
        print "[C]harmander], [S]quirtle, or [B]ulbasaur."
        continue
    // Echo the user's choice
    print "You chose: " + userChoice
    choices = ['C', 'S', 'B']
    opponentChoice = random.choice(choices)
    print "I chose: " + opponentChoice
    
    
    if opponentChoice == str.upper(userChoice):
        print "Tie! "
    #if opponenetChoice == str("C") and str.upper(userChoice) == "S"
    elif opponentChoice == 'C' and userChoice.upper() == 'B':      
        print "Charmander beats rock, I Bulbasaur! "
        continue
    elif opponentChoice == 'B' and userChoice.upper() == 'S':      
        print "Bulbasaur beats Squirtle! I win! "
        continue
    elif opponentChoice == 'S' and userChoice.upper() == 'C':      
        print "Squirtle beat Charmander, I win! "
        continue
    else:       
        print "You win!"

