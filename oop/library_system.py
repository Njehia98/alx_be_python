class Book:
    def __init__(self, title, author):
        """Initialize the base Book class."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for Book objects."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook, calling the Book constructor."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for EBook objects."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook, calling the Book constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for PrintBook objects."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize a Library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
