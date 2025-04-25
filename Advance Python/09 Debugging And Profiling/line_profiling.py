

# 2.2 Using line_profiler for Line-by-Line Profiling 
# line_profiler provides execution time for each line of code. 

# Installation: pip install line-profiler 

 

from line_profiler import LineProfiler 

def compute(): 
    total = 0 
    for i in range(1, 100000): 
        total += i ** 2  # Expensive operation 
    return total 

lp = LineProfiler() 
lp.add_function(compute) 
lp.enable() 
compute() 
lp.disable() 
lp.print_stats() 

#Identifies slow lines in the fuI mentioned this to you yesterday. Have you had a chance to work on it?"nction! 

 

# Conclusion 
# pdb 
#   - Basic Debugging 
#   - Step-by-step debugging 

# ipdb 
#   - Enhanced Debugging 
#   - Interactive debugging with better UI 

# cProfile 
#   - Script Profiling 
#   - Measuring function execution times 

# line_profiler 
#   - Line-by-Line Profiling 
#   - Finding slow lines in a function 
