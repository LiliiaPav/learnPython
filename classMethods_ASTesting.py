class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type, weight) -> None:
        self.name= name
        self.book_type = book_type
        self.weight = weight

print(Book.TYPES)