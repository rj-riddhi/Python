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


# Write a program to sum first n natural numbers.
def sum(n):
    if n == 1:
        return 1
    return sum(n-1)+n
print(f"First 4 number sum is {sum(4)}")

def func():
    try:
        print("Edu", end="")
    finally:
        print("reka!")
func()