# Datatypes
# 1) Integer
# 2) Float
# 3) String
# 4) None

# Rules
# - can contain digits, underscores and alphabets
# - can only start with alphabets and underscore
# - cant't start with digit
# - no white space  allowed while defining a variable
# - special characters are not allowed


a = 1 #integer
b = 2
c = 4.4 #float 
name = "Radhika" #string
is_valid = True #boolean
d = None #none datatype 
print(a+2)

# operators
# Arithmetic operators: +, -, *, / 
# Assignment opeartors: = , +=, -+
# Comparison operators: == , > , >=, < , <= (reurns always boolean answer True/False ), !=
# Logical Operators: or, and
# not 
print(not(True))

# type - to identify type of a variable
print(type("Radhika"))
print(type(1))

# type casting - used to convert valid variable to desired type variable
name = "31.2"
print(type(name))
float_num = float(name)
print(float_num)
print(type(float_num))


# Important interview question
print(f"{1.0 == 1}") # It will return True as values are same, For float and int values only
print(f"{"1.0" == 1}") # It will return False as datatypes are different