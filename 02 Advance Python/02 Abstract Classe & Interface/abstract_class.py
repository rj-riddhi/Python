''' Abstract classes and interfaces in Python are tools for creating blueprints for other classes. 
 They provide a way to enforce certain methods and properties in subclasses, promoting consistency and code reusability. '''

 

''' 
An abstract class is a class that cannot be instantiated directly. 
It can contain: 
1)Abstract methods (methods without implementation that must be defined in child classes). 
2)Concrete methods (methods with implementation that can be inherited by child classes). 
'''

# Python provides the ABC (Abstract Base Class) module in the abc package for creating abstract classes. 

 

'''
Key Points About Abstract Classes 
- Cannot Be Instantiated: You cannot create an instance of an abstract class. 
- Abstract Methods: These are methods declared but not implemented in the abstract class. Subclasses must implement them. 
- Concrete Methods: Abstract classes can have concrete methods that subclasses inherit. 
'''
 

from abc import ABC, abstractmethod 

class Animal(ABC): 

    @abstractmethod 
    def sound(self): 
        """Abstract method to be implemented by subclasses""" 
        pass 

    def sleep(self): 
        """Concrete method""" 
        print("Sleeping...") 

class Dog(Animal): 

    def sound(self): 
        return "Woof!" 

class Cat(Animal): 

    def sound(self): 
        return "Meow!" 

dog = Dog() 
cat = Cat() 
print(dog.sound())  
print(cat.sound()) 
dog.sleep() 
