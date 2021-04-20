# Joshua Sells, Intro to computer science, 10/20/2019, program_6.py, this program creates shapes and then draws them.

from turtle import Turtle
import random

class Shape():
    turtle = Turtle()

class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def get_area(self):
        return 3.14* self.radius*self.radius
    def draw(self):
        Shape.turtle.penup() 
        Shape.turtle.setposition(self.center[0], self.center[1] - self.radius)
        Shape.turtle.pendown() 
        Shape.turtle.circle(self.radius) 
        Shape.turtle.penup()
        
class Rectangle(Shape):
    def __init__(self, upper_left, lower_right):
        self.upper_left = upper_left
        self.lower_right = lower_right
    def get_area(self):
        return ((abs(self.lower_right[0]-self.upper_left[0])) * (abs(self.upper_left[1]-self.lower_right[1])))
    def draw(self):
        Shape.turtle.penup()
        Shape.turtle.setposition(self.upper_left)
        Shape.turtle.pendown()
        Shape.turtle.goto(self.lower_right[0], self.upper_left[1])
        Shape.turtle.goto(self.lower_right)
        Shape.turtle.goto(self.upper_left[0], self.lower_right[1])
        Shape.turtle.goto(self.upper_left)
        Shape.turtle.penup()
        
class RightTriangle(Shape):
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
    def get_area(self):
        return ((abs((self.point_a[0]-self.point_b[0])) * abs((self.point_a[1]-self.point_b[1]))) / 2)
        
    def draw(self):
        Shape.turtle.penup()
        Shape.turtle.setposition(self.point_a)
        Shape.turtle.pendown()
        Shape.turtle.goto(self.point_b)
        Shape.turtle.goto(self.point_b[0], self.point_a[1])
        Shape.turtle.goto(self.point_a)
        Shape.turtle.penup()

def random_shapes(count):
    def random_point():
        return (random.randint(-200,200), random.randint(-200,200))
    shapes = []
    for i in range(1, count+1):
        shape_type = random.randint(1, 3)
        if shape_type == 1:
            shapes+=[Circle(random_point(), random.randint(1,200))]
        elif shape_type == 2:
            shapes+=[Rectangle(random_point(), random_point())]
        else:
            shapes+=[RightTriangle(random_point(), random_point())]      
    return shapes

def main():
    shapes = random_shapes(15)
    total_area = 0
    for s in shapes:
        s.draw()
        total_area += s.get_area()

    input("Hit <enter> key to end.")
    print("total area = ", total_area)
    input("Good bye!")

main()