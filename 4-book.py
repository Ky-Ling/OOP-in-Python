'''
Date: 2022-02-25 18:46:16
LastEditors: GC
LastEditTime: 2022-02-25 19:21:37
FilePath: \OOP in Python\4-book.py
'''

class Book:

    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def print_info(self):
        print(self.title + " is written by " + self.author)

    # If I wanna represent a book, let me just represent it by its title
    def __repr__(self) -> str:
        return self.title

    
