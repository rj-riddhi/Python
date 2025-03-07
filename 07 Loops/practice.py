# write a program to print multiplication table of given number
print("Using for loop")
num = int(input("enter number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
    i += 1

# using while loop
print("Using while loop s")
i = 1
while(i<11):
    print(f"{num} X {i} = {num*i}")
    i += 1


# write a program to check whether given number is prime or not
print("Check number is prime or not")
num = int(input("Enter number: "))
for i in range(2,num):
    if num%i == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")

# Write a program to find a first n number sum
sum = 0
num = int(input("Enter number: "))
for i in range(1, num+1):
    sum += i
    i += 1
print(f"sum is {sum}")

# Write a program to find factorial of given number
num = int(input("Enter number: "))
product = 1
for i in range(1, num+1):
    product *= i
    i += 1
print(f"factorial is {product}")





