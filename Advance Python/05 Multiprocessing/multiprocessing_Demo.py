# The multiprocessing module in Python allows you to create multiple processes to run tasks in parallel. 
# Unlike threads, processes have separate memory space, meaning the Global Interpreter Lock (GIL) does not affect them. 
# This makes the multiprocessing module ideal for CPU-bound tasks (e.g., mathematical computations or data processing). 

# Key Features of multiprocessing 
# Parallelism: Each process runs independently, taking full advantage of multiple CPU cores. 
# Isolation: Processes have their own memory space, avoiding data corruption issues found in threads. 
# Inter-process Communication (IPC): Data can be shared between processes using queues, pipes, or shared variables. 


# Example: 

import multiprocessing 
import time 

def worker_process(name, delay, count): 
    for i in range(count): 
        time.sleep(delay) 
        print(f"Process {name}: {i}") 

if __name__ == "__main__": 
    process1 = multiprocessing.Process(target=worker_process, args=("P1", 1, 5)) 
    process2 = multiprocessing.Process(target=worker_process, args=("P2",0.5,5)) 
    process1.start() 
    process2.start() 
    process1.join() 
    process2.join() 
    print("Main process execution completed.")

# Explanation 
# Process Creation: 
# A process is created using multiprocessing.Process(). 
# target specifies the function to be run in the process. 
# args provides the arguments for the target function. 

# Starting Processes: 
# process1.start() starts the process, running the target function in a new process. 

# Joining Processes: 
# process1.join() ensures the main process waits until process1 has completed its execution. 

# Output: 
# Processes run in parallel. The output will not necessarily follow a sequential order due to the independent nature of processes. 
 

# Advantages of multiprocessing 
# Better for CPU-bound Tasks: Processes bypass the GIL, allowing true parallelism for CPU-heavy tasks like computations. 
# Isolation: Processes do not share memory, avoiding race conditions without needing synchronization mechanisms. 
 

# When to Use multiprocessing 
# CPU-bound tasks: Large computations or tasks that require heavy processing. 
# Parallel execution: When tasks need to run independently and truly in parallel. 