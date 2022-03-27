'''
Date: 2022-02-25 15:43:54
LastEditors: GC
LastEditTime: 2022-02-25 19:21:09
FilePath: \OOP in Python\3.py
'''

# 1: Class method:

class Person:
    number_of_people = 0

    def __init__(self, name) -> None:
        self.name = name
        Person.add_class()

    # This method is activated on this class itself
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_class(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Brian")

Person.number_of_people_()


# 2: Static method:

class Math:
    @staticmethod
    def add5(x):
        return x + 5

print(Math.add5(3))
