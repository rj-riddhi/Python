class Employee:
    salary = 1200000  # This is class attribute
    language = "Python"

object = Employee()
object.name = "Radhika" # This is  /instance attribute
print(f"name  of object is {object.name}")
print(f"salary of this object is: {object.salary}")
print(f"language of this object is: {object.language}")

# Instance attribute take prefrence first over class attribute, here below is example 
class InstanceVsClassAttribute:
    attributeType = "class"

object2 = InstanceVsClassAttribute()
object2.attributeType = "Instance"
print(f"Instance attribute take prefrence first over class attribute {object2.attributeType}")

 
# terms
# Noun => class => Emplyee
# Adjective => ttributes => name, language
# Verbs => methods => getSalary() 