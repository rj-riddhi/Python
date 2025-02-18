# List is a container to store the data of any datatype
print("List in pythons")
friends = ["Radhika", "Apple", 1, 0.45, True]
print("Print the list:", friends)
print("First element is:", friends[0])

#list are mutable bt strings are immutable here below is example
# name = 'Radhika'
# name[0] = 'P' # will give error
# print("String is:", name)

friends[0] = "Heena" # will replace first element
print("New list:", friends)

# List slicing
print("Sliced list:", friends[0:2])

# List methods (stores to original list, it changes the original list)
print(friends)
friends.append("hello")  # Will add element at the end of the list
print(friends)
friends.insert(1,"parmar") # Will add element at the given index
print(friends)
friends.reverse() # Will reverse element
print(friends)
print(friends.pop(0)) # Will remove element from the given index and return the popped element  
print(friends)
friends.remove("parmar") # Will remove perticular given element
print(friends)

