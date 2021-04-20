# Joshua Sells, Intro to computer science, 09/22/2019, lab_3.py, this program computes your tax rate and net annual pay.

def main ():
    
    # get name
    name = getName ()
    
    # get gross pay
    grossPay = getGrossPay ()
    
    # get number of dependents
    numberOfDependents = getNumberOfDependents ()
    
    # calculate tax bracket
    taxBracket = calcTaxBracket (numberOfDependents)
    
    # calculate net pay
    netPay = calcNetPay (grossPay, taxBracket)
    
    # print results
    print('Name:      ', name)
    print('Gross pay:  $', format(grossPay, '.2f'), sep='')
    print('Dependents:', numberOfDependents)
    print('Tax rate:  ', format(taxBracket, '.0%'))
    print('Net pay:    $', format(netPay, '.2f'), sep='')    
    
# define getName function
def getName ():
    userInput = input('Enter your name: ')
    return userInput

# define getGrossPay funtion
def getGrossPay ():
    userInput = float(input('Enter your gross pay: '))
    return userInput

# define getNumberOfDependants function
def getNumberOfDependents ():
    userInput = int(input('Enter number of dependents: '))
    return userInput

# define calculate tax bracket function
def calcTaxBracket (dependents):
    if dependents == 0 or dependents == 1:
        result = 0.2
    elif dependents == 2 or dependents == 3:
        result = 0.15
    elif dependents >= 4:
        result = 0.1
    return result

# define calcNetPay function
def calcNetPay (gross, bracket):
    result = gross - (gross * bracket)
    return result

# call the main function
main()