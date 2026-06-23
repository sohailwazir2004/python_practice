# Task 1: Rectangle Class
# Write a Rectangle class in Python that lets you build a rectangle with length and width attributes.

# Create a Perimeter() method to calculate the perimeter.
# Create an Area() method to calculate the area.
# Create a display() method that shows the length, width, perimeter, and area.

class Rectangle():
    def __init__(self,l,w):
        self.length  = l
        self.width = w

   
    def perimeter(self):
        return 2*(self.length +self.width)
        
    def area(self):
        return self.length*self.width
    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area()) 
                
obj = Rectangle(20,10)

obj.display()