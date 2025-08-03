class Book:
    def __init__(self, author, title,):
        self.author = author
        self.title = title
        self.is_checked_out = False
        
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self.is_checked_out
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library:
    
    def __init__(self):
        self._books = []
        
    def check_out_book(self,title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available:
                book.return_book()
                return
            
    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(book)
        