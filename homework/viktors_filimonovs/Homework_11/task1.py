class Book:
    page_material = "paper"
    test_presence = True

    def __init__(self, book_title, author,
                 page_numbers, isbn, reserved_book=False):
        self.book_title = book_title
        self.author = author
        self.page_numbers = page_numbers
        self.isbn = isbn
        self.reserved_book = reserved_book

    def __str__(self):
        status = ", зарезервирована" if self.reserved_book else ""
        return (f"Название:{self.book_title}, Автор: {self.author}, "
                f"страниц: {self.page_numbers}, "
                f"Material: {self.page_material}{status}")


class SchoolBooks(Book):
    def __init__(self, book_title, author,
                 page_numbers, isbn, subject, school_class, tasks=False,
                 reserved_book=False):
        super().__init__(book_title, author, page_numbers, isbn,
                         reserved_book=reserved_book)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def __str__(self):
        status = ", зарезервирована" if self.reserved_book else ""
        return (f"Название:{self.book_title}, Author: {self.author}, "
                f"страниц: {self.page_numbers}, "
                f"предмет: {self.subject}, "
                f"класс: {self.school_class}{status}")


books = [
    Book("Идиот", "Достоевский", 500, "978-5-389-07487-1"),
    Book("Война и мир", "Толстой", 1225, "978-5-389-07487-1",
         reserved_book=True),
    Book("Преступление и наказание", "Достоевский", 671, "978-5-389-07487-1"),
    Book("Мастер и Маргарита", "Булгаков", 480, "978-5-389-07487-1"),
    Book("Вий", "Гоголь", 320, "978-5-389-07487-1",
         reserved_book=True)

]


study_books = [
    SchoolBooks("Алгебра", "Konako", 145, "978-5-389-07487-1",
                "математика", "8", reserved_book=True),
    SchoolBooks("Геометрия", "Konako", 457, "978-5-389-07487-1",
                "математика", "9"),
    SchoolBooks("Физика", "DR.Dre", 157, "978-5-389-07487-1", "физика", "9",
                reserved_book=True),
    SchoolBooks("История", "Держинский", 457, "978-5-389-07487-1",
                "история", "6"),
    SchoolBooks("Биология", "Васелькова", 457, "978-5-389-07487-1",
                "биология", "9"),
    SchoolBooks("Философия", "Кант", 457, "978-5-389-07487-1",
                "философия", "9"),

]

print("📚 Books")
for book in study_books:
    print(book)

print(30 * "=")

print("\n📖 School Books")
for book in books:
    print(book)
