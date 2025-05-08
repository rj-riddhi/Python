# An environment variable (also known as "env var") is a variable that lives outside of the Python code, in the operating system, and could be read by your Python code (or by other programs as well).
# Environment variables could be useful for handling application settings, as part of the installation of Python, etc.

import os

name = os.getenv("MY_NAME", "world")
print(f"Hello {name} from Python")