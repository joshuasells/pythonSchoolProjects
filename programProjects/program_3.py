# Joshua Sells, Intro to computer science, 09/22/2019, program_3.py, this program is a simple command line calculator.

# delcare global variable for usage statistics

addCount = 0
subCount = 0
mulCount = 0
divCount = 0
absCount = 0

def main ():
    print('Welcome to iCalculator.')
    
    keepGoing = True
    
    while keepGoing == True:
        userInput = input('>')
        tokens = userInput.split(' ')
        
        #add operation
        if tokens[0] == 'add':
            print(add(tokens[1], tokens[2]))
            global addCount
            addCount += 1
        
        #subtract operation
        elif tokens[0] == 'sub':
            print(sub(tokens[1], tokens[2]))
            global subCount
            subCount += 1
        
        #multiply operation
        elif tokens[0] == 'mul':
            print(mul(tokens[1], tokens[2]))
            global mulCount
            mulCount += 1
        
        #divide operation
        elif tokens[0] == 'div':
            print(div(tokens[1], tokens[2]))
            global divCount
            divCount += 1
            
        #absolute value operation. This function is built in so I didn't have to define it.
        elif tokens[0] == 'abs':
            print(abs(float(tokens[1])))
            global absCount
            absCount += 1
        
        #quits the program and displays the stats
        elif tokens[0] == 'quit':
            quit()
            keepGoing = False

# define add function
def add (num1, num2):
    return float(num1) + float(num2)

# define sub function
def sub (num1, num2):
    return float(num1) - float(num2)

# define mul function
def mul (num1, num2):
    return float(num1) * float(num2)

# define div function
def div (num1, num2):
    if num2 == '0':
        print('Error: Division by zero')
        return 0
    else:
        return float(num1) / float(num2)

# define quit function
def quit ():
    print('Function usage count')
    print('add function : ', addCount)
    print('sub function : ', subCount)
    print('mul function : ', mulCount)
    print('div function : ', divCount)
    print('abs function : ', absCount)
    
main()