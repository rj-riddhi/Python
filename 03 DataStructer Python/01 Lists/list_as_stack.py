
# List As A Stack 
# The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. 

stack = [3, 4, 5] 
stack.append(6) 
stack.append(7) 
print(f"Stack is: {stack}")
 
stack.pop() # 7 will get removed (last in first out) 
print("Last in First out: pop()")
print(f"Stack is: {stack}")
print(f"Stack is: {stack}")
stack.pop() # 6 will get removed 
stack.pop() # 5 will get removed 
print(f"Stack is: {stack}")