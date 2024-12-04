from ioutils import JSONIO
from book import Book


class Library:
    def __init__(self):
        lib = JSONIO.read("../books.json")
        self._books: dict[int, Book] = {
            book.get("id"): Book.from_dict(book) for book in lib.get("books", {})}
        Book.set_next_id(lib.get("next_id"))

    def add_book(self, title: str, author: str, year: str) -> None:
        new_book: Book = Book(title=title, author=author, year=year)
        self._books[new_book.id] = new_book
        JSONIO.write("../books.json", {
            "books": [book.to_dict() for book in self._books.values()],
            "next_id": Book.get_next_id(),
        })
        print("Книга добавлена")

    def delete_book(self, id: int) -> None:
        a = self._books.pop(id, None)
        print(self._books, a)
        if a:
            JSONIO.write("../books.json", {
                "books": [book.to_dict() for book in self._books.values()],
                "next_id": Book.get_next_id(),
            })
            print("Книга удалена")
        else:
            print("Такой книги не существует!")

    def find_books(self, query: str):
        book_ids: list[int] = []
        books_list: list[Book] = [book for book in self._books.values()]
        tokens: list[str]
        query = query.lower()

        if query == "":
            tokens = []
        elif len(query.strip(" ")) == 0:
            tokens = [" "]
        else:
            tokens = query.strip().split(" ")

        for book in books_list:
            for token in tokens:
                if token in book.get_search_string():
                    book_ids.append(book.id)
                    break
        return tuple(book_ids)

    def print_books(self, book_ids: tuple[int] = None) -> None:
        if self.size <= 0:
            print("\nБиблиотека пуста!\n")
        elif book_ids != None:
            print(f"Книг найдено по запросу - {len(book_ids)}:")
            for id in book_ids:
                book: Book = self._books.get(id, None)
                if book:
                    print(f"- {book}")
                else:
                    print(f"Ошибка! Книга с id: {id} не найдена в библиотеке.")
                    break
        else:
            print(f"Книг в библиотеке на данный момент - {self.size}:")
            for book in self._books.values():
                print(f"- {book}")

    def change_status(self, id: int, status: int) -> None:
        book = self._books.get(id, None)
        if book:
            book.status = status
        else:
            print("Такой книги не существует!")

    @property
    def size(self) -> int:
        return len(self._books)
