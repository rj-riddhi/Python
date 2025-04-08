# It is a group statement performing a specific task.
# It can be reused n number of times in a programm
# print average

# Function without arguments
print("Function without arguments")
# Function defination
def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    avg = (a+b+c)/3
    print(f"Average is {avg}\n")
# Function call
avg()  

# function with arguments
print("Function with arguments")
def avg(a,b,c):
    avg = (a+b+c)/3
    print(f"Average is {avg}\n")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
avg(a,b,c)


# Write a program to greet a user with Good day
def greet(name):
    print(f"Good day {name}")
greet(input("Enter your name: "))

# Function with return values
def sum(a,b):
    return (a+b)
a = int(input("Enter number: "))
b = int(input("Enter number: "))
sum = sum(a,b)
print(sum)

# Default value
# We can have default value as a argument, when value is not given in param default value argument will be used
def defVal(name,ending="Hello"):
    print(name,ending)
name=input("Enter your name")
defVal(name)

# Arbitary Arguments, *args 
def my_function(*kids): 
  print("The youngest child is " + kids[2]) 
 
my_function("Emil", "Tobias", "Linus")  