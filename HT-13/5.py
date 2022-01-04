# 5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).


class Book(object):
    _name: str

    def __init__(self, name):
        self._name = name

    def __key(self):
        return self._name

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.get_name() == other.get_name()
        return NotImplemented

    def get_name(self):
        return self._name


# a-lya singleton
class Library(object):
    _instance = None
    _list_of_books_names = []
    _books = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    @staticmethod
    def add_book(temp_book: Book):
        Library._books.setdefault(temp_book, 0)
        Library._books[temp_book] += 1
        Library._list_of_books_names.append(temp_book.get_name())

    @staticmethod
    def get_book(temp_book: Book):

        if Library._books.get(temp_book, -1) > 0:
            Library._books[temp_book] -= 1
            return temp_book
        else:
            print("we dont have it :(")
            return None

    @staticmethod
    def print_journal_of_books():
        for book, quantity in Library._books.items():
            print(book.get_name(), quantity)


def main():
    library = Library()
    list_of_titles = [
        "In Search of Lost Time Ulysses",
        "Don Quixote",
        "One Hundred Years of Solitude",
        "The Great Gatsby",
        "Moby Dick",
        "War and Peace",
        "Hamlet"
    ]
    list_of_books = [Book(title) for title in list_of_titles]

    for book in list_of_books:
        Library.add_book(book)

    Library.print_journal_of_books()

    tom = Book("Adventures of Tom Sawyer")
    whale = Book("Moby Dick")

    print(f"get {tom.get_name()}")
    if Library.get_book(tom):
        print(tom.get_name())
    print(f"get {whale.get_name()}")
    if Library.get_book(whale):
        print(whale.get_name())

    Library.print_journal_of_books()

if __name__ == "__main__":
    main()
