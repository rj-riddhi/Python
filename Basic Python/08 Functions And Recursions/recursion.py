# Recursion is a function which calls itself
# Need to make surefunction doesn't go into infinite

def factorial(n):
    if n == 1 or n == 0 :
       return 1 
    return n * factorial(n-1)
n = int(input("Enter number: "))
print(f"factorial of number {n} is {factorial(n)}")