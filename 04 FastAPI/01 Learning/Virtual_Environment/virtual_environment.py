# When you work in Python projects you probably should use a virtual environment (or a similar mechanism) to isolate the packages you install for each project.

# A virtual environment is different than an environment variable.
# An environment variable is a variable in the system that can be used by programs.
# A virtual environment is a directory with some files in it.

# Create a Virtual Environment:
    # When you start working on a Python project for the first time, create a virtual environment inside your project.
    # You only need to do this once per project, not every time you work.
# Command: python -m venv .venv
    # python: use the program called python
    # -m: call a module as a script, we'll tell it which module next
    # venv: use the module called venv that normally comes installed with Python
    # .venv: create the virtual environment in the new directory .venv

# Activate the Virtual Environment:
# Activate the new virtual environment so that any Python command you run or package you install uses it.
# Do this every time you start a new terminal session to work on the project.
# Command: source .venv/bin/activate
# Every time you install a new package in that environment, activate the environment again.Every time you install a new package in that environment, activate the environment again.

# Check the Virtual Environment is Active:
# Command: which python or revious command


# Deactivate Virtual Environment
# Command: deactivate
print("Hello world")