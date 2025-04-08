 

# Lists, tuples, dictionaries, and sets are all iterable objects.  
# They are iterable containers which you can get an iterator from. 
# All these objects have a iter() method which is used to get an iterator: 

# Difference between iterator and for loop
#  Iterator is object while for loop is A control structure
#  Iterator uses explicitly (iter(), next()) while for loop implicitly (calls __iter__() and __next__() under the hood)
#  In Iterator You can manually control when to get the next value while in for loop it Automatically fetches each item until the end
#  Iterator Can raise StopIteration error while for loop Handles StopIteration internally

mytuple = ("apple", "banana", "cherry") 
myit = iter(mytuple) 

print(next(myit)) 
print(next(myit)) 
print(next(myit)) 
# print(next(myit)) # will raise StopIteration error