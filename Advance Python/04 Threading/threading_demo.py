# The threading module in Python is used to run multiple threads concurrently. 
# A thread is a separate flow of execution, and Python allows us to work with threads to achieve multitasking within a program. 

 

# Key Points About threading: 
# Concurrency: Threads allow a program to run multiple operations at once, though due to the Global Interpreter Lock (GIL) in CPython, threads in Python are more suited for I/O-bound tasks (like network requests or file I/O) than CPU-bound tasks. 
# Lightweight: Threads are lightweight compared to processes. 
# Shared Memory: Threads within the same process share memory, making data sharing easier, but this requires synchronization mechanisms to avoid race conditions. 


import threading 
import time 

def print_numbers(name, delay, count): 
    for i in range(count): 
        time.sleep(delay) 
        print(f"{name}: {i}") 

# Create threads 
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 1, 5)) 
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 0.5, 5)) 

# Start threads 
thread1.start() 
thread2.start() 

# Wait for threads to finish 
thread1.join() 
thread2.join() 
print("Main thread execution completed.") 


# Explanation 
# Creating a Thread: 
# A thread is created using threading.Thread(). 
# target specifies the function to run in the thread. 
# args provides the arguments for the target function. 

# Starting a Thread: 
# thread1.start() starts the thread execution. The function passed to target begins running in the thread. 

# Joining a Thread: 
#  thread1.join() blocks the main thread until thread1 has completed its execution. 

# Shared Execution: 
# Both threads run concurrently. Due to the time.sleep() calls, the output alternates between threads. 