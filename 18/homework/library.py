class Book:
    def __init__(self, title, author=None, year=None):
        if author is None:
            author = ''
        if year is None:
            year = ''
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"{self.title:<30}{self.author:<20}{self.year:>5}")


class Library:
    def __init__(self, name, book_list=None):
        if book_list is None:
            book_list = []
        self.name = name
        self.book_list = book_list

    def list(self):
        for book in self.book_list:
            book.display()

    def filter(self, title=None, author=None, year=None):
        if title is None:
            title = ''
        if author is None:
            author = ''
        if year is None:
            year = ''
        filtered_list = []
        if title == '' and author == '' and year == '':
            return self.book_list
        else:
            for book in self.book_list:
                if title.lower() == book.title.lower() or author.lower() == book.author.lower() or year == book.year:
                    filtered_list.append(book)
        return filtered_list

    def add_book(self, book):
        self.book_list.append(book)

    def delete_book(self, book):
        self.book_list.remove(book)

    @staticmethod
    def as_table(books):
        print(f"{'Название':<30}{'Автор':<20}{'Год':>5}")
        for book in books:
            print(f"{book.title:<30}{book.author:<20}{book.year:>5}")


book_1 = Book('Чистый код', 'Дядя Боб', 2017)
book_2 = Book('От 2 до 5', 'Корней Чуковский', 1958)
book_3 = Book('Идеальный программист', 'Дядя Боб', 2018)
book_4 = Book('Рецепты татарской кухни', year=2018)

library = Library('Домашняя библиотека')
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)
print(library.name)
library.list()

books = library.filter(author="Дядя боб")
books[0].display()


books = library.filter(author='дядя боб')
Library.as_table(books)
