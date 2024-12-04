from library import Library
from book import Book
from ui import draw_menu
from userinput import get_number_from_user, get_user_action


def mainloop(library: Library) -> None:
    while True:
        draw_menu()
        action: int = int(get_number_from_user("Выберите действие: "))
        if action == 1:
            title: str = input("Введите название книги: ").strip()
            author: str = input("Введите автора книги: ").strip()
            year: str = get_number_from_user("Введите год издания книги: ")
            library.add_book(title=title, author=author, year=year)
        elif action == 2:
            id: int = int(get_number_from_user(
                "Введите id книги для удаления: "))
            library.delete_book(id)
        elif action == 3:
            print(
                """
Для поиска книг введите критерии поиска.
Можно заполнить только нужные поля, оставив остальные пустыми.
                """
            )
            query: str = input("Введите поисковый запрос: ")
            book_ids: tuple[int] = library.find_books(query=query)
            library.print_books(book_ids=book_ids)
        elif action == 4:
            library.print_books()
        elif action == 5:
            id: int = int(get_number_from_user("Введите id книги: "))
            print("0 - Выдана\n1 - В наличии")
            status: int = int(get_number_from_user("Выберите статус: "))
            library.change_status(id, status)
        elif action == 6:
            break
        else:
            print("Неизвестное действие!")


def main() -> None:
    library: Library = Library()
    mainloop(library)


if __name__ == "__main__":
    main()
