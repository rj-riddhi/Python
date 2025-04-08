#  Set is a collection of non repetitive elements

s = set() # Empty set , Don't use s = {} as it will create empty dictionary
s.add(1)
s.add(2)
print(s)

y = {3,4}
print(f"Type: {type(y)}")

# Methods
s.add(3)
print(f"Add method: {s}")
print(f"Length method: {len(s)}")
s.remove(2)
print(f"Remove method: {s}")
s.clear()
print(f"Clear method: {s}")

# Properties
# 1.) Unordered
# 2.) Unindexed -> cannot access elements by index 
# print(f"First element is {s[0]}") # Not valid
# 3.) Items cannot changed in set it is meaningless bcz it contains well defined uniq values
# 4.) Cannot contain duplicate values.


# Union and intersection in set
s1 = {1,2,3,4}
s2 = {4,5,6,7}
print(f"Union: {s1.union(s2)}")
print(f"Intersection: {s1.intersection(s2)}")
print(f"{2.0 == 2}")

# Remove item from set
thisset = {"apple", "banana", "cherry"} 
thisset.remove("banana") 
print(thisset) 
# {'cherry', 'apple'} 

#  If the item to remove does not exist, remove() will raise an error. 
thisset.discard("banana") # NOT raise an error. 
print(thisset) 

# Interview Question
s1 = {1,2,3}
s2 = {3,4,5}
s1.intersection_update(s2)
print(s1)
 