# Local Scope
def myfunc():
    x = 300
    print(x)

myfunc()

# Local variable accessed from a nested function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# Global Scope
x = 300

def myfunc():
    print(x)

myfunc()
print(x)

# Same variable name in local and global scope
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()
print(x)

# Global Keyword - make a variable global from inside a function
def myfunc():
    global x
    x = 300

myfunc()
print(x)

# Nonlocal Keyword - refer to variable in the outer (enclosing) function
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())
