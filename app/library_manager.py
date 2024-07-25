from file_helpers import save, load_data, update
from models import Book
from exceptions import NotFoundException, InvalidFieldException, InvalidStatusException


class LibraryDatabase:

    def __init__(self) -> None:
        self.path = "library.json"

    def save_book(self, book: dict[str, str]):
        save(book, self.path)

    def load_books(self):
        return load_data(self.path)

    def update_books(self, books: dict[str, str]):
        return update(books, self.path)


class Librarian:

    def __init__(self) -> None:
        self.db = LibraryDatabase()

    def add_book(self, title: str, author: str, year: str) -> None:
        new_book = Book(title, author, year)
        try:
            new_book_dict = vars(new_book)
            self.db.save_book(new_book_dict)

            print(f"\nBook has been saved successfully.\nID: {new_book_dict['id']}")
        except Exception as e:
            print(f"\nError saving the book: {e}")

    def delete_book(self, id: str) -> None:
        try:
            del_book = self._get_by_id(id)
            books = self._load_books()["books"]
            books.pop(del_book)
            self.db.update_books(books)
            print(f"\nBook {id} has been deleted successfully.")

        except NotFoundException:
            print(f"\nBook with ID {id} not found.")
        except Exception as e:
            print(f"\nError deleting the book: {e}")

    def serch_book(self, key: str, value: str):
        try:
            if key.lower() not in ("id", "author", "title", "year", "status"):
                raise InvalidFieldException

            books = self.db.load_books()["books"]
            res_books = [book for book in books if book.get(key.lower()) == value]

            if res_books:
                for b in res_books:
                    print(f"\n{Librarian._formater(b)}")
            else:
                raise NotFoundException

        except InvalidFieldException as e:
            print(f"\nInvalid field '{key}'.{e}")
        except NotFoundException:
            print(f"\nNo books found with {key} = '{value}'.")
        except Exception as e:
            print(f"Error searching for the book: {e}")

    def get_all_books(self):
        books = self.db.load_books()["books"]
        for b in books:
            print(f"\n{Librarian._formater(b)}")

    def change_status(self, id: str, new_status: str):
        try:
            if new_status not in ("в наличии", "выдана"):
                raise InvalidStatusException

            index = self._get_by_id(id)
            books = self.db.load_books()["books"]
            books[index]["status"] = new_status
            self.db.update_books(books)
            print(f"\nBook status has been changed successfully.")

        except InvalidStatusException as e:
            print(f"\nInvalid status '{new_status}'.{e}")
        except NotFoundException:
            print(f"\nBook with ID {id} not found.")
        except Exception as e:
            print(f"\nError changing book status: {e}")

    def _get_by_id(self, id: str) -> int | None:
        books = self.db.load_books()["books"]
        for i, book in enumerate(books):
            if book["id"] == id:
                return i
            else:
                raise NotFoundException

    @staticmethod
    def _formater(book_dict: dict[str, str]) -> str:
        string = ["Book"]
        for k, v in book_dict.items():
            string.append(f"{k}: {v}")

        return ", ".join(string)


l = Librarian()

l.add_book("f", "GG", "12345")
l.serch_book("GG", "s")
