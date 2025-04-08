# if elif else ladder
a = int(input("Enter your age: "))
if a >= 18 :
    print("You are the above age of consent")
    print("Good for you")    
elif a < 0 :
    print("You are entering wrong age")
elif a == 0 :
    print("O is not a valid age")
else :
    print("You are the below age of consent")
    
print("End of program")

# Relational Operators
#  == , >= , <= 
# Logical Operators
# and, or, not

# short hand if statement
a = 34 
b = 33 
if a > b: print("a is greate")

# short hand of if..else
a = 33
print('a is greater') if a > b else print("a is equal")