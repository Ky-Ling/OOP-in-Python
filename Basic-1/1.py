'''
Date: 2022-02-25 14:22:09
LastEditors: GC
LastEditTime: 2022-02-25 14:39:11
FilePath: \OOP in Python\1.py
'''

class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []

    # Add a student object to this course
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Tim", 14, 99)
s2 = Student("Brian", 16, 85)
s3 = Student("David", 19, 76)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())
