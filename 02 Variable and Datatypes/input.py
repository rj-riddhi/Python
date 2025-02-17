# input() this is used to take an input from user side
a = input("Enter first number:") # this takes user input as a string
print("the type of input is ",type(a))
b = input("Enter second number:")

c = int(input("Enter third number:"))
print("Type of third number is", type(c))

print("Number a is:", a)
print("Number b is:", b) 
print("Sum is:", int(a) + int(b)) 


# fsting => print variable inside the string
name = input("Enter your name")
print(f"Good Afternoon {name}")