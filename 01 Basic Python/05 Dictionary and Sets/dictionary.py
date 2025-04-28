# Dictionary is a set of key,value pair datatype in python
# It is mutable
# Mutable: Dictionary, List
# Immutable: String, Tuples
marks = {} # Empty disct.
marks = {
    'Radhika': 100,
    'Sapana': 90,
    "Gudi": 80,
    "List": [1,2,3]
}

for x, y in marks.items():
  print(x, y)

print(f"Type: {type(marks)} \nMarks: {marks}")
print(marks["Radhika"])
print(marks['List'])
print(len(marks))

# Properties of Dict.
# 1) Unordered
# 2) Mutable
# 3) Indexed
# 4) Cannot contain duplicate keys

# Methods
print(f"items mehod: {marks.items()}")   # Returns list of (key,value) Tuples
print(f"keys method: {marks.keys()}") # Returns list of keys
print(f"values method: {marks.values()}")
marks.update({'Gudi': 90, "Renuka": 34})  #  It is possible because dictionary in python is mutable
print(f"update method: {marks}")  # Updates the dictionary with supplied key-value pairs 
print(f"get method: {marks.get('Radhika')}")

print("Diff of get method and marks['key']")
print(f"Using get: {marks.get('Hello')}") # Returns None as key is not present
# print(f"Print using [] {marks["Hello"]}") # Will give error and breaks the code



marks.clear()
print(f"Clear method: {marks}")