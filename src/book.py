
class Book:
    _id: int
    _title: str
    _author: str
    _year: str
    _status: int  # TODO: придумать как удобно реализовать значение статуса

    _next_id: int = 0
    _search_fields: tuple[str] = ("_title", "_author", "_year")

    def __init__(self, title: str, author: str, year: str) -> None:
        self._id = Book._next_id
        Book._next_id += 1
        self._title = title
        self._author = author
        self._year = year
        self._status = 1
        print("asd", Book._next_id)

    def __repr__(self) -> str:
        return f"Id: {self._id}, Title: {self._title}, Author: {
            self._author}, Year: {self._year}, Status: {self.status}"

    def to_dict(self) -> dict[str, str | int]:
        books_dict = {key[1:]: value for key,
                      value in vars(self).items() if key[0] == "_"}
        return books_dict

    @classmethod
    def from_dict(cls, data: dict[str, str | int]) -> "Book":
        attrs: tuple[str] = (
            "title",
            "author",
            "year",
        )
        new_book: "Book" = cls(**{attr: data.get(attr) for attr in attrs})
        new_book.id = data.get("id")
        return new_book

    def get_search_string(self) -> str:
        return "".join([getattr(self, attr) for attr in self._search_fields]).lower()

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int) -> int:
        self._id = id

    @property
    def year(self) -> int:
        return int(self._year)

    @property
    def status(self) -> int:
        status_text: dict[int, str] = {
            0: "Выдана",
            1: "В наличии",
        }
        return status_text.get(self._status)

    @status.setter
    def status(self, status: int) -> None:
        if status in (0, 1):
            self._status = status
        else:
            print("Статус не был изменен, неверный код статуса!")

    @classmethod
    def get_next_id(cls) -> int:
        return cls._next_id

    @classmethod
    def set_next_id(cls, id: int) -> None:
        cls._next_id = id
