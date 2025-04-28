
# Interfaces 
# An interface is a more rigid form of abstraction where only abstract methods are defined. All methods in an interface must be implemented by the subclass. 
# Python does not have a direct keyword for interfaces, but you can achieve it using abstract classes with only abstract methods. 

# Key Points About Interfaces 
#  All methods in an interface are abstract. 
# Subclasses must implement all methods of the interface. 
# No method in the interface can have an implementation. 
 

from abc import ABC, abstractmethod 

class Shape(ABC): 

    @abstractmethod 
    def area(self): 
        pass 

    @abstractmethod 
    def perimeter(self): 
        pass 
 
class Rectangle(Shape): 

    def __init__(self, width, height): 
        self.width = width 
        self.height = height 

    def area(self): 
        return self.width * self.height 

    def perimeter(self): 
        return 2 * (self.width + self.height) 

class Circle(Shape): 

    def __init__(self, radius): 
        self.radius = radius 

    def area(self): 
        return 3.14 * self.radius ** 2 

    def perimeter(self): 
        return 2 * 3.14 * self.radius

rect = Rectangle(5, 10) 
circle = Circle(7) 

print("Rectangle Area:", rect.area()) 
print("Rectangle Perimeter:", rect.perimeter()) 
print("Circle Area:", circle.area()) 
print("Circle Perimeter:", circle.perimeter()) 