

# 2. Profiling for Performance Optimization 
# Profiling helps identify performance bottlenecks by measuring execution time. 

# 2.1 Using cProfile for Function Profiling 
# cProfile provides detailed profiling statistics for an entire script. 

 

import cProfile 

def slow_function(): 
    total = 0 
    for i in range(1, 100000): 
        total += i 
    return total 

cProfile.run("slow_function()") 

 
# Output shows execution time for each function call. 