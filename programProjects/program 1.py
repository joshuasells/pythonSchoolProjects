# Joshua Sells, Intro to computer science, 09/08/2019, program_1.py, this program computes your tax bill!!!.

#prompt user for first name, last name, monthly gross pay, number of dependents.

name = input('Enter your name: ')
grossPay = float(input('Enter your gross pay: '))
numberOfDependents = int(input('Enter number of dependents: '))

#calculate tax bracket

if numberOfDependents == 0 or numberOfDependents == 1:
    taxBracket = 0.2
elif numberOfDependents == 2 or numberOfDependents == 3:
    taxBracket = 0.15
elif numberOfDependents >= 4:
    taxBracket = 0.1

#calculate net pay

netPay = grossPay - (grossPay * taxBracket)

#print results

print('Name:      ', name)
print('Gross pay:  $', format(grossPay, '.2f'), sep='')
print('Dependents:', numberOfDependents)
print('Tax rate:  ', format(taxBracket, '.0%'))
print('Net pay:    $', format(netPay, '.2f'), sep='')

input('press enter to exit')

