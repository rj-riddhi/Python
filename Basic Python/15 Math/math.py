# Built-in Math Functions
x = min(5, 10, 25)  # returns the smallest value
y = max(5, 10, 25)  # returns the largest value

print(x)  # 5
print(y)  # 25

# abs() returns the absolute value
x = abs(-7.25)
print(x)  # 7.25

# pow(x, y) returns x raised to the power of y
x = pow(4, 3)
print(x)  # 64

# Math Module
import math

# sqrt() returns the square root
x = math.sqrt(64)
print(x)  # 8.0

# ceil() rounds a number up to the nearest integer
# floor() rounds a number down to the nearest integer
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)  # 2
print(y)  # 1

# math.pi returns the value of pi
print(math.pi)  # 3.141592653589793
