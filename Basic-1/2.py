'''
Date: 2022-02-25 14:40:10
LastEditors: GC
LastEditTime: 2022-02-25 15:40:32
FilePath: \OOP in Python\2.py
'''

# Inheritance in OOP:

class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old!")

    def speak(self):
        print("I do not know what to say")

class Cat(Pet):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and my color is {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark") 

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.speak()

c = Cat("Bill", 90, "white")
c.speak()
c.show()

d = Dog("Joe", 12)
d.speak()

# If there is a method defined in the lower-level class or the child class that is the same name as the upper level class,
#   it will automatically override that method. 

f = Fish()
f.speak()