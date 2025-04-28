# The asyncio module in Python is designed to handle asynchronous programming.
# allowing you to run tasks concurrently without needing multiple threads or processes. 
# It is particularly well-suited for I/O-bound tasks like web scraping, network operations, or reading/writing files. 

 

# Key Concepts of asyncio: 

# 1) Coroutines:  
#     -  Coroutines are special functions defined with async def. They are designed to be paused and resumed using await. 
#     -  A coroutine doesn’t execute immediately but returns a coroutine object. 

# 2) Event Loop: 
#     - asyncio uses an event loop to manage the execution of coroutines. 
#     - The event loop schedules tasks and handles their execution. 

# 3) Concurrency: 
#     - Tasks run concurrently but not in parallel (as in threading or multiprocessing). 

# 4) await: 
#     - Pauses the coroutine until the awaited task is completed, allowing other tasks to run in the meantime. 

import asyncio 

async def fetch_data(task_name, delay): 
    print(f"{task_name}: Starting") 
    await asyncio.sleep(delay) 
    print(f"{task_name}: Finished after {delay} seconds") 

async def main(): 
    task1 = asyncio.create_task(fetch_data("Task 1", 2)) 
    task2 = asyncio.create_task(fetch_data("Task 2", 1)) 
    task3 = asyncio.create_task(fetch_data("Task 3", 3)) 
    print("All tasks started.") 
    await task1 
    await task2 
    await task3 
    print("All tasks completed.") 

asyncio.run(main()) 

 

# Explanation 
# Defining a Coroutine:  async def fetch_data: Defines a coroutine function. 
# await asyncio.sleep(delay): Simulates an I/O operation and allows other tasks to run during the sleep. 
# Creating Tasks: asyncio.create_task() schedules the coroutine to run concurrently as an independent task. 
# Concurrency: Tasks run concurrently. For example, Task 2 can complete while Task 1 and Task 3 are sleeping. 
# Event Loop: asyncio.run(main()) starts the event loop and executes the main coroutine. 

# Advantages of asyncio 
#     - Efficient I/O-bound Task Management: Ideal for tasks like downloading data, web scraping, or querying databases. 
#     - Non-blocking: While one task is waiting, other tasks can execute. 
#     - Scalable: Supports thousands of tasks without the overhead of threads or processes. 

# When to Use asyncio 
#     - I/O-bound tasks: Fetching data from APIs, querying databases, or file I/O. 
#     - Real-time applications: Chat applications, live dashboards, or event-driven systems. 
 