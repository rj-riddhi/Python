# List Comprehensions 

# List comprehensions provide a concise way to create lists. 
# Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition. 

# For example, assume we want to create a list of squares, like: [0,1,2,4,9]
squares = [] 
 
# Tradditional way
# >>> for x in range(10): 
# ...  squares.append(x**2) 
# ... 
# >>> squares 
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 

# or, equivalently: 
squares = [x**2 for x in range(4)] 
print(squares)
# which is more concise and readable. 


# A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. For example, this listcomp combines the elements of two lists if they are not equal: 
list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] 
print(list)