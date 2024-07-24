from file_helpers import save, load_data, update
from models import Book


class Librarian:

    def __init__(self) -> None:
        self.path = "library.json"

    def _save_book(self, book: dict[str, str]):
        save(book, self.path)

    def _load_books(self):
        return load_data(self.path)

    def _update_books(self, books: dict[str, str]):
        return update(books, self.path)

    def _get_by_id(self, id: str) -> int | None:
        books = self._load_books()["books"]
        for i, book in enumerate(books):
            if book["id"] == id:
                return i

    def add_book(self, title: str, author: str, year: str) -> None:
        new_book = Book(title, author, year)
        try:
            new_book_dict = vars(new_book)
            self._save_book(new_book_dict)

            print(f"\nBook has been saved successfully.\nID: {new_book_dict['id']}")
        except Exception as e:
            print(f"Error saving the book: {e}")

    def delete_book(self, id: str) -> None:
        del_book = self._get_by_id(id)
        if del_book:
            try:
                books = self._load_books()["books"]
                books.pop(del_book)
                self._update_books(books)

                print(f"\nBook {id} has been deleted successfully.")
            except Exception as e:
                print(f"Error deleting the book: {e}")
        else:
            print(f"\nThere is no book with id: {id}")

    def serch_book(self, key: str, value: str):
        if key.lower() in ("id", "author", "title", "year", "status"):
            books = self._load_books()["books"]
            res_books = []
            for book in books:
                if book[key.lower()] == value:
                    res_books.append(book)

            if res_books:
                for b in res_books:
                    print(f"\n{Librarian._formater(b)}")
            else:
                print(f"\nThe book with {key}: {value} was not found")

    @staticmethod
    def _formater(book_dict: dict[str, str]) -> str:
        string = ["Book"]
        for k, v in book_dict.items():
            string.append(f"{k}: {v}")

        return ", ".join(string)


l = Librarian()

l.add_book("1", "A", "12344")
l.add_book("2", "B", "12344")
l.delete_book("59175f94-2024-07-24")
l.add_book("34", "Bфф", "12344")
l.serch_book("author", "A")
l.serch_book("author", "AAAA")
