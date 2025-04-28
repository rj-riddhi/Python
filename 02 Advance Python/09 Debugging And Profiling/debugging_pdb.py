# Debugging and profiling are crucial for identifying and resolving issues in Python applications.
#  Let's explore advanced debugging tools (pdb, ipdb) and performance profiling (cProfile, line_profiler). 

# 1. Advanced Debugging Tools 
# 1.1 Using pdb (Python Debugger) 

# The pdb module provides an interactive debugging environment. 
# Example: Debugging with pdb 

import pdb 

def divide(a, b): 
    pdb.set_trace()
    result = a / b 
    return result 
print(divide(10, 2)) 

 
 

# How to Use pdb: 
# When running the script, it will pause at pdb.set_trace(). You can then use commands like: 
# n (next line) 
# s (step into function) 
# p variable (print variable) 
# c (continue execution) 
 

 