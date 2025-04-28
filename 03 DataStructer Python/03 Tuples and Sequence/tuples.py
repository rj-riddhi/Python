# What is a Tuple?
# A tuple is like a list, but immutable.
# ✅ Ordered
# ✅ Can hold elements of any type
# ✅ Duplicates allowed
# 🚫 Cannot be changed after creation (no add/remove)

# Example
my_tuple = (1, 2, 3, "hello", 3.14)
print(my_tuple)

# Create:
t = (1, 2, 3)
print(t)

# Single-element tuple:
t = (5,) # (comma is important!)
print(t)

# Access elements:
print(t[0])

# Slicing:
print(t[1:3])

# Membership test	
print(2 in t)

# Can be nested:	
t = (1, (2,3))
print(t)


# Cannot modify	
t[0] = 10  #will give error

# Why use Tuples instead of Lists?
# Data Safety: Protects data from accidental changes.
# Faster: Slightly faster than lists because they're fixed.
# Hashable: Tuples can be used as dictionary keys and set elements (if they contain only hashable items).
