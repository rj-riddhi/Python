# What is a Dictionary?
#    - A collection of key-value pairs.
#    - Unordered
#    - Mutable (you can change, add, remove items).

# Keys must be unique and immutable (like strings, numbers, tuples).
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(my_dict)

# ✅ Quick lookup by key
# ✅ Keys must be unique
# ✅ Values can be anything (even lists, dicts, etc.)


# Create dictionary:
d = {"a":1, "b":2}	
print(d)

# Access value:
print(d["a"])

# Update value:
print(f"before change: {d['a']}")
d["a"] = 100
print(f"after change: {d['a']}")

# Add new pair:	
d["c"] = 300
print(d)

# Delete pair:
del d["b"]
print(d)

# Length:
print(len(d))	#number of key-value pairs

# Membership check:
print("a" in d)

# Important Dictionary Methods
# get(key, default)	Safely get value
# keys():	Returns all keys
# values():	Returns all values
# items():	Returns (key, value) pairs
# pop(key):	Removes key and returns its value
# update(other_dict):	Updates dict with another dict
# clear():	Removes all items

# Dictionary Comprehensions (Super Cool!)
# Just like list comprehensions — you can build dicts quickly:


# Squares of numbers
squares = {x: x**2 for x in range(5)}
print(squares) 

# Nested Dictionaries
# You can have dictionaries inside dictionaries:

students = {
    "101": {"name": "Alice", "marks": 85},
    "102": {"name": "Bob", "marks": 90}
}

print(students["101"]["name"]) 