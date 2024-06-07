# Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods.
# Show that your program doesn't persist the books after the program is stopped!


class Library:
    def __init__(self):
        self.books: list[str] = []
        self.no_of_books: int = 0

    def print_books(self) -> None:
        for book in self.books:
            print(f'- {book}')

    def add_book(self, new_book: str) -> None:
        self.books.append(new_book)
        self.no_of_books += 1

    def get_no_of_books(self) -> int:
        return self.no_of_books


def main() -> None:
    library: Library = Library() # Creates an instance of Library.

    # Prints initial library details.
    print(f'Library has {library.get_no_of_books()} books, which are: ')
    library.print_books()
    print()

    while True:
        # Inputs a book to add to library.
        book: str = input('Enter a book to add to library or enter q to quit: \n')

        if book.lower() == 'q':
            break

        if not book:
            print('Enter a book to add to Library!\n')
            continue

        library.add_book(book)
        print(f"'{book}' book has been added to the library.\n")

    # Prints final details if user quits the program.
    print()
    print(f'Library has {library.get_no_of_books()} books, which are: ')
    library.print_books()


if __name__ == '__main__':
    main()
