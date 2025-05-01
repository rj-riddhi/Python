# Fast api:
# -> It is a python web framework
# -> Provides automatic documentations - provides swagger ui for created apis to test and check the responses
# -> Also provide redock UI

# Run main.py file using following command, 
# Command: fastapi dev main.py 
# or: uvicorn main:app --reload


# Virtual Environment:
# Create a Virtual Environment: python -m venv .venv 
# Activate the Virtual Environment: source .venv/bin/activate 
# Check the Virtual Environment is Active: which python 

# When you work in Python projects you probably should use a virtual environment (or a similar mechanism) to isolate the packages you install for each project. 

# - A virtual environment is different than an environment variable. 
# - An environment variable is a variable in the system that can be used by programs. 
# - A virtual environment is a directory with some files in it. 


# Every time you install a new package in that environment, activate the environment again. 
# This makes sure that if you use a terminal (CLI) program installed by that package, you use the one from your virtual environment and not any other that could be installed globally, probably with a different version than what you need. 

 

# Environment Variable:
# Create and Use Env Vars: You can create and use environment variables in the shell (terminal), without needing Python
# You could create an env var MY_NAME with 
export MY_NAME="Wade Wilson" 

# Then you could use it with other programs, like 
# echo "Hello $MY_NAME" 

import os 
name = os.getenv("MY_NAME", "World") 
print(f"Hello {name} from Python") 

 