# Joshua Sells, Intro to computer science, 10/19/2019, lab_7.py, this program prompts for rectangle dimensions and return the area.

def main():
    
    validation = False
    
    while validation == False:
        try:
            height = input('Enter height: ')
            int(height)
            validation = True
        except:
            print(height, 'is not a valid input. Try again.')
            
    validation = False
    
    while validation == False:
        try:
            width = input('Enter width: ')
            int(width)
            validation = True
        except:
            print(width, 'is not a valid input. Try again.')
            
    print('The area is', int(height)*int(width))
            
main()