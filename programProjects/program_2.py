# Joshua Sells, Intro to computer science, 09/11/2019, lab_2.py, this is a simple dice game.

import random

# Welcome user to the game.

print('Welcome to Dice Game.')
print()
print('You are given $250 to start.')
print("You can't play once you run out of money.")

bankRoll = 250

# Initiate game in a while loop.

keepPlaying = True

while keepPlaying == True:
    print()
    
# Get the bet Amount.
    
    betAmount = int(input('How much are you betting? '))

# Confirm the bet amount is correct.
    
    while betAmount > bankRoll or betAmount < 0:
        betAmount = int(input('Please enter an appropriate betting amount. '))
    
    print('Rolling the dice.....')

# Get the player's guess.
    
    playerGuess = int(input('What is the sum of the two dice? '))

# Confirm the player's guess is correct.

    while playerGuess < 2 or playerGuess > 12:
        playerGuess = int(input('Please enter an appropriate sum of the dice. '))

    dieOne = random.randrange(1,7)
    dieTwo = random.randrange(1,7)
    sumOfDice = dieOne + dieTwo
    
    print('Die 1 is', dieOne)
    print('Die 2 is', dieTwo)
    
# If the player is correct, than reward them.
    
    if playerGuess == sumOfDice:
        if dieOne == dieTwo:
            bonus = betAmount * 2
            print('You win $', bonus, sep='')
            bankRoll += bonus
        else:
            print('You win $', betAmount, sep='')
            bankRoll += betAmount
            
# Otherwise, if the player is wrong, then penalize them.
    else:
        print('You lost $', betAmount, sep='')
        bankRoll -= betAmount

    print('Your current balance is $', bankRoll, sep='')

# If the player is out of money, then they are done.

    if bankRoll == 0:
        print('Sorry, you are out of money.')
        print('See you later!')
        keepPlaying = False
        
# Otherwise, ask them if they want to play another game.

    else:
        userDecision = input('Do you want another game? Y/N: ')
        
# Confirm they are using the correct format.

        while userDecision != 'Y' and userDecision != 'y' and userDecision != 'N' and userDecision != 'n':
            userDecision = input('Please answer with Y/N format. ')
            
# If the player wants to be done, then thank them for playing.

        if userDecision == 'N' or userDecision == 'n':
            print('Thank for playing, see you later!')