# Test-Driven Development (TDD) is a software development approach where tests are written before the actual implementation code. 

# The cycle of TDD consists of three main steps: 
# Red: Write a test that fails because the functionality is not implemented yet. 
# Green: Implement the minimum amount of code required to pass the test. 
# Refactor: Improve the code while ensuring the test still passes. 

# To run test file: python3 -m unittest [testfilename]

class Calculator:
    def add(self, a, b): 
        return a + b 

    def subtract(self, a, b): 
        return a - b 

    def multiply(self, a, b): 
        return a * b 

    def divide(self, a, b): 
        if b == 0: 
            raise ZeroDivisionError("Cannot divide by zero") 
        return a / b