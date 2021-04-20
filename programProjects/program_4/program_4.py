# Joshua Sells, Intro to computer science, 09/29/2019, program_4.py, this program performs operations with files.

def main():
    
    again = True
    
    #display options
    
    while again == True:
        print('Choose an option:')
        print('1. Load data')
        print('2. Display computed statistics')
        print('3. Save computed statistics')
        print('4. Exit')
        
        #get user choice
        choice = input('Choice: ')
        
        #validate user choice
        while choice != '1' and choice != '2' and choice != '3' and choice != '4':
            choice = input('Please enter 1-4: ')
        print()
        #load data   
        if choice == '1':
            reprompt = True
            while reprompt == True:
                grades = loadData(input('Enter the name of the file: '))
                if grades != None:
                    print('Data read successfully.')
                    print()
                    reprompt = False
        
        #display computed statistics
        elif choice == '2':
            try:
                print('Below are the computed values:')
                print('Min    =', min(grades))
                print('Max    =', max(grades))
                print('Mean   =', format(mean(grades), '.1f'))
                print('Median =', format(median(grades), '.0f'))
                print()
            except UnboundLocalError:
                print('Must load data first')
                print()
        
        #save computed statistics to a file.
        elif choice == '3':
            saveData(input('Enter the name of the file: '), grades)
            print('Data saved successfully')
            print()
            
        #Goodbye!
        else:
            again = False
            print('Goodbye!')

#captures the data in the file and assign it to a list named grades.
def loadData(fileName):
    try:
        gradesFile = open(fileName, 'r')
        grades = (gradesFile.read()).split()
        gradesFile.close()
        for i in range(len(grades)):
            grades[i] = int(grades[i])
        return grades
    except FileNotFoundError:
        print('ERROR: file does not exist')

#calculates the mean.        
def mean(grades):
    total = 0
    
    for i in grades:
        total += i
        
    mean = total / len(grades)
    return mean

#calculates the median.
def median(grades):
    grades.sort()
    
    length = len(grades)
    if length % 2 == 0:
        median = grades[length//2-1]
    else:
        median = grades[(length-1)//2]
    return median

#saves the calculated data to a txt file.
def saveData(fileName, grades):
    try:
        statsFile = open(fileName, 'w')
        statsFile.write('Min    = ' + str(min(grades)) + '\n')
        statsFile.write('Max    = ' + str(max(grades)) + '\n')
        statsFile.write('Mean   = ' + str(format(mean(grades), '.1f')) + '\n')
        statsFile.write('Median = ' + str(format(median(grades), '.0f')) + '\n')
    except:
        print('An error occured')

main()