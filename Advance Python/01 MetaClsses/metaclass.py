# - In Python, a metaclass serves as a blueprint for creating classes, 
# - similar to how a class serves as a blueprint for creating objects. 
# - It defines the behavior of classes and allows for customization of class creation. 
# - Every class in Python is an instance of a metaclass, with the default metaclass being type.

# Key Points About Metaclasses 
# What is a Metaclass? 
# It is a class that creates classes. 
# Classes are instances of a metaclass. 

# Why Use Metaclasses? 
# To control or modify the creation of classes. 
# To enforce certain rules or patterns for class definitions. 
# To automatically add or modify attributes or methods in a class. 

# How Classes Are Created? 
# When you define a class, Python uses its metaclass (default is type) to create it. 

# Defining a Custom Metaclass 
# A custom metaclass is defined by subclassing type and overriding one or more of its methods, like __new__ and __init__. 
# Key Methods in Metaclasses 
# __new__(cls, name, bases, dct): Creates and returns a new class object. It is called before __init__. 
# __init__(cls, name, bases, dct): Initializes the class after it has been created. 


class MyMeta(type): 
    def __new__(cls, name, bases, dct): 
        print(f"Creating class {name}") 
        dct['greet'] = lambda self: f"Hello from {name}!" 
        return super().__new__(cls, name, bases, dct) 

class MyClass(metaclass=MyMeta): 
    def __init__(self): 
        self.name = "MyClass Instance" 

 
obj = MyClass() 
print(obj.greet()) 