# Class definition
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an Object
person1 = Person("Alice", 30)

print(person1.name)
person1.greet()