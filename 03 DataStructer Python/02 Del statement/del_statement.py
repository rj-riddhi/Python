# There is a way to remove an item from a list given its index instead of its value
# This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example: 


a = [-1, 1, 66.25, 333, 333, 1234.5] 
del a[0]
print(f"Used index inside del like del a[0]: {a} ")
 
del a[2:4] #includes position 2 but not 4  
print(f"Used slice inside del like del a[2:4]: {a}")
 
del a[:] # without position it will delete whole aray  
print(f"Used slice without any position inside del like del a[:]: {a}")

# del can also be used to delete entire variables: 
del a 
print(f"Used del to delete entire variable like del a: {a}")