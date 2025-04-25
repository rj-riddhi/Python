'''
    *
   ***
  *****
'''

n = int(input("Enter number: "))
for i in range(1,n+1):
    print(" "*(n-i), end="")     # in print statement end="" argument is used if we don't want new line after print statement
    print("*"*((2*i)-1)) 
    i+=2

'''
*
**
***
'''
n == int(input("Enter number: "))
for i in range(1,n+1):
    print("*"*i)


'''
***
* *
***
'''
n == int(input("Enter number: "))
for i in range(1,n+1):
    if (i == 1 or i == n):
         print("*"*n, end="")
    else:
        print("*", end="")
        print(" ", end="")
        print("*", end="")
    print("")