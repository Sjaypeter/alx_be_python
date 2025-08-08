class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
        
class EBook(Book):
    def __init__(self, file_size:int):
        self.file_size = file_size
        
class PrintBook(Book):
    def __init__(self, page_count:int):
        self.page_count = page_count
        
class Library(Book):
    def __init__(self, book):
        self.book = []
        
    def add_book(self,book):
        self.book.append(book)
        
    def list_books(self):
        return f"{Book.title} by {Book.author}"
        
        