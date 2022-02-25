'''
Date: 2022-02-25 19:13:30
LastEditors: GC
LastEditTime: 2022-02-25 21:35:58
FilePath: \OOP in Python\5-Library.py
'''

class Library:

    def __init__(self) -> None:
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out(self, title, name):
        for book in self.books:
            if book.title == title:
                book.check_out(name)
                return
        print("Book is not found!")

 