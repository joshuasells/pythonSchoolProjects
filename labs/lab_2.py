# Joshua Sells, Intro to computer science, 09/11/2019, lab_2.py, this program does various tasks using loops.

###############################################################################################################
#1. print integers in sequences of ten going up to 100.

for x in range(0, 101, 10):
    print(x)

input('press enter to move on to the next program')

###############################################################################################################
#2. generate 10 random number and print the average.

# Method 1: (this is what I initially did. I used an array/list, but then remembered that you probably wanted us to use an accumulator.

import random

randomNumbers = []

for x in range(10):
    randomNumbers.append(random.randrange(1,501,2))
    print(randomNumbers[x])

average = float(sum(randomNumbers)/10)
print('The Average of the numbers is:', average)

input('press enter to move on to the next program')

# Method 2: I used an accumulator.

import random

total = 0

for x in range(10):
    num = random.randrange(1,501,2)
    
    print(num)
    total += num
    
average = float(total/10)
print('The Average of the numbers is:', average)

input('press enter to move on to the next program')

###############################################################################################################
#3. print whatever the user inputs and stop when they type, 'done'. Use a break statement.

while True:
    userInput = input('say something: ')
    print('you said:', userInput)
    if userInput == 'done':
        break

print('Goodbye!')

input('press enter to move on to the next program')

###############################################################################################################
#4. do the same as #3 but use a condition instead of a break statement.

keepGoing = True

while keepGoing == True:
    userInput = input('say something: ')
    print('you said:', userInput)
    if userInput == 'done':
        keepGoing = False

print('Goodbye!')

input('press enter to move on to the next program')