# Create a class
class MyClass:
    x = 5

# Create object
p1 = MyClass()
print(p1.x)

# The __init__() function
# The __init__() function is called automatically every time the class is being used to create a new object. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# The __str__() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

# Object methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Modify object properties
p1.age = 40

# Delete object properties
del p1.age

# Delete object
del p1
