# Nested List Comprehensions 

# The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension. 

# Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4: 
matrix = [ 
[1, 2, 3, 4], 
[5, 6, 7, 8], 
[9, 10, 11, 12], 
] 

# The following list comprehension will transpose rows and columns: 
print(f"{[[row[i] for row in matrix] for i in range(4)]}")

# In the real world, you should prefer built-in functions to complex flow statements. 
# The zip() function would do a great job for this use case: 
print(f"Using zip method: {list(zip(*matrix))}")

 

# zip() function: 
# Syntax: zip(*iterables, strict=False) 
# Iterate over several iterables in parallel, producing tuples with an item from each one. 

# Example: 
for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item) 