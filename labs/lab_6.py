# Joshua Sells, Intro to computer science, 10/20/2019, lab_6.py
#This program create a number of rectangle objects and prints the dimensions and total area.

class Rectangle:
    
    #the __init__ method initializes a rectangles height and width attributes.
    def __init__(self, height, width):
        self.height = int(height)
        self.width = int(width)
        
    def computeArea(self):
        return self.height * self.width
        
def main():
    
    import random
    
    numOfRectangles = random.randrange(1, 11)
    print('The number of rectangles is', numOfRectangles)
    print()
    
    rectList = []
    
    for i in range(numOfRectangles):
        rectList.append(Rectangle((random.randrange(1, 101)), (random.randrange(1, 101))))
    
    totalArea = 0
    
    for obj in rectList:
        print('[', obj.height, ', ', obj.width, ']', sep='')
        totalArea += (obj.computeArea())
    print()
    
    print('The total area is', totalArea)
    
main()
    