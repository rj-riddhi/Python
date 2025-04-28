# List As A Queues 
# It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one). 

# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. 

from collections import deque 
 
queue = deque(["Eric", "John", "Michael"]) 
queue.append("Terry") 
print("Terry Arrives")
queue.append("Graham")
print("Graham Arrives")
print(f"Used append method in Deque which appends at the end bydefault: {queue}")

queue.popleft()                
print(f"first to arrive now leaves, Eric Leavs: {queue} ")

queue.popleft()
print(f"The second to arrive now leaves, John leavs: {queue}")