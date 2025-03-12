# Write a program to find gratest of given three number
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
c = int(input("Enter number three: "))



def maxNum(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c 
n = maxNum(a,b,c)
print(f"Max number is {n}")