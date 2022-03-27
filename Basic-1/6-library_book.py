'''
Date: 2022-02-25 20:44:00
LastEditors: GC
LastEditTime: 2022-02-25 21:26:49
FilePath: \OOP in Python\6-library_book.py
'''

from book import Book

class LibraryBook(Book):
    
    def __init__(self, title, author, inventory) -> None:
        # Call a method of a superclass
        super.__init__(title, author)

        self.inventory = inventory
        self.borrowers = []

    def check_out(self, name):
        
        if self.inventory < 1:
            print("Sorry, not available")
            return

        # When I check out a book and we will decrease the inventory and add the person's name whoever check out the book to
        #   the list of borrowers.  
        self.inventory -= 1
        self.borrowers.append(name)
        
    def print_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Inventory Remaining: {self.inventory}")
        print(f"Borrowers: {', '.join(self.borrowers)}")
        