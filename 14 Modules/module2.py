import module1 
# or
# import module1 as md
 
module1.greeting("Jonathan") # Access method

a = module1.person1["age"]  # Access variable values
print(a) 

# Built in module
import platform 
 
x = platform.system() 
print(x) 

# If we want to import only variable or method
from module1 import person1
print(person1["name"])