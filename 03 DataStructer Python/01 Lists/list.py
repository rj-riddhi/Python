# Lists are used to store multiple items in a single variable. 
# Lists are created using square brackets for ex. test_list = ['abc','xyz',123] 
# List items are ordered, changeable, and allow duplicate values. 
# List items are indexed, the first item has index [0], the second item has index [1] etc. 
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created. 

# List Methods 
# append() - Adds an element at the end of the list 
# Syntax: list.append(x) 
fruits = ['apple', 'banana', 'cherry'] 
fruits.append("orange") 
print(f"Appende method: {fruits}")

# clear() - Removes all the elements from the list 
# Syntax: list.clear() 
fruits = ['apple', 'banana', 'cherry', 'orange'] 
fruits.clear() 
print(f"Clear method: {fruits}")
 
# copy() - Returns a copy of the list 
# Syntax: list.copy() 
fruits = ['apple', 'banana', 'cherry', 'orange'] 
x = fruits.copy() 
print(f"Copy method: {x}")

# count() - Returns the number of elements with the specified value 
# Syntax: list.count(x) 
fruits = ['apple', 'banana', 'cherry'] 
x = fruits.count("cherry") 
print(f"Count method: {x}")

# extend() - Add the elements of a list (or any iterable), to the end of the current list 
# Syntax: list.extend(iterable) 
fruits = ['apple', 'banana', 'cherry'] 
cars = ['Ford', 'BMW', 'Volvo'] 
fruits.extend(cars) 
print(f"Extend method: {fruits}")

# index() - Returns the index of the first element with the specified value 
# Syntax: list.index(x) 
fruits = [4, 55, 64, 32, 16, 32] 
x = fruits.index(32) 
print(f"Index method: {x}")

# insert() - Adds an element at the specified position 
# Syntax: list.insert(i, x) 
fruits = ['apple', 'banana', 'cherry'] 
fruits.insert(1, "orange") 
print(f"Insert method: {fruits}")

# pop() - Removes the element at the specified position 
# Syntax: list.pop([i]) 
fruits = ['apple', 'banana', 'cherry'] 
fruits.pop(1) 
print(f"Pop method: {fruits}")

# remove() - Removes the item with the specified value 
# Syntax: list.remove(x) 
fruits = ['apple', 'banana', 'cherry'] 
fruits.remove("banana") 
print(f"Remove method: {fruits}")

# reverse() - Reverses the order of the list 
# Syntax: list.reverse() 
fruits = ['apple', 'banana', 'cherry'] 
fruits.reverse() 
print(f"Reverse method: {fruits}")

# sort() - Sorts the list 
# Syntax: list.sort(*, key=None, reverse=False) 
cars = ['Ford', 'BMW', 'Volvo'] 
cars.sort(reverse=True) 
print(f"Sort method: {cars}")