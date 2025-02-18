# Tuples is like a list but it is an immutable datatype in python
a = (1,2,3,4,"Hello",False)
print(f"Type is: {type(a)} and length is {len(a)} and tuple is {a}")

# Empty tuple
b = ()
print(f"Type is: {type(b)} and length is {len(b)}")

# Define tuple with only one element
c = (1) # Not valid, it will become int like c = 1
print(f"Type is: {type(c)}")
c = (1,) # Valid tuple with only one value
print(f"Type is: {type(c)} and length is {len(c)}")

# Tuple is an immutable datatype
# a[0] = 0 # Will give an error
# print(a)

# Tuple methods => Like a string tuples are immutable so in every method it will return new tuple as a result and original tuple will remain same
print(a)
print(f"Length method: {len(a)}")
print(f"Count method: {a.count(1)}")
print(f"Index method: {a.index("Hello")}") # Will raise an error if given element is not present in tuple
print(f"Slicing of tuple: {a[0:4]}")
print(f"Concatinate two tuples: {a + ("new", "tuple")}")
e = (1,2,3) 
print(f"Min method: {min(e)}")
print(f"Max method: {max(e)}")

l = [1,2,3,4,5]
print(f"sum is: {sum(l)}")