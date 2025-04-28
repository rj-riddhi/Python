# Method Resolution Order (MRO) is the order in which Python looks for a method or attribute in a hierarchy of classes. It determines the sequence in which base classes are searched when a method is called on an instance of a derived class. 
# The MRO is particularly important in multiple inheritance scenarios to ensure that methods are called in the correct order and to prevent ambiguity or redundancy. 

 

# How MRO Works 
# Python uses the C3 Linearization Algorithm (also known as the "C3 superclass linearization") to determine the MRO. 
# The key properties of this algorithm are: 
# Preserves Local Precedence Order: A class precedes its parents in the MRO. 
# Preserves Monotonicity: The MRO of the parent classes is preserved. 
# Left-to-Right Order: In multiple inheritance, the order of the base classes matters. 

 

# You can view the MRO of a class using:  
# ClassName.__mro__ 
# ClassName.mro() (returns a list) 

 

# for single inheritance 
class A: 
    def show(self): 
        print("A") 

class B(A): 
    pass 

b = B() 
b.show()  # A 
print(B.mro())  #[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>] 
# Explanation: The MRO of B is B → A → object. Python looks for the show method in B, then in A, and finally in object. 

# For multiple inheritance 
class A: 
    def show(self): 
        print("A") 

class B: 
    def show(self): 
        print("B") 

class C(A, B): 
    pass 

c = C() 
c.show()  #A 
print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>] 

# Explanation: 
# C inherits from A and B. 
# Since A is listed first in C(A, B), Python looks for the show method in A first, then in B. 

# Diamond problem 
class A: 
    def show(self): 
        print("A") 

class B(A): 
    def show(self): 
        print("B") 

class C(A): 
    def show(self): 
        print("C") 

class D(B, C): 
    pass 

d = D() 
d.show()  # B 
print(D.mro())  #[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>] 

# Explanation: 
# D inherits from B and C, and both inherit from A. 
# MRO for D ensures B is searched before C (left-to-right order), and A is searched only once. 

 

# How MRO is Determined (C3 Linearization) 
# - Start with the class itself. 
# - Add the parent classes in the order they are listed in the class definition. 
# - Merge the MRO of parent classes while maintaining the order. 

 

# Practical Applications of MRO 
# - Resolving ambiguities in multiple inheritance. 
# - Ensuring consistent behavior in inheritance hierarchies. 
# - Debugging complex class relationships. 