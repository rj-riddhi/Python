# Import JSON module
import json

# ------------------------------
# Convert from JSON string to Python dict
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y)  # {'name': 'John', 'age': 30, 'city': 'New York'}

# ------------------------------
# Convert from Python dict to JSON string
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)
print(y)  # {"name": "John", "age": 30, "city": "New York"}

# ------------------------------
# Convert different Python data types to JSON strings
print(json.dumps({"name": "John", "age": 30}))        # {"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"]))               # ["apple", "bananas"]
print(json.dumps(("apple", "bananas")))               # ["apple", "bananas"]
print(json.dumps("hello"))                            # "hello"
print(json.dumps(42))                                 # 42
print(json.dumps(31.76))                              # 31.76
print(json.dumps(True))                               # true
print(json.dumps(False))                              # false
print(json.dumps(None))                               # null

# ------------------------------
# Format the result with indentation
x = {"name": "John", "age": 30}
print(json.dumps(x, indent=4))
# {
#     "name": "John",
#     "age": 30
# }

# ------------------------------
# Use custom separators
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# {
#     "name" = "John". 
#     "age" = 30
# }

# ------------------------------
# Sort keys in the output
print(json.dumps(x, indent=4, sort_keys=True))
# {
#     "age": 30,
#     "name": "John"
# }
