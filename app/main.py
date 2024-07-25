from library_manager import Librarian


def main():
    library = Librarian()
    menu: dict = {
        "\n1": "Add book",
        "2": "Delete book",
        "3": "Search book",
        "4": "Get all books",
        "5": "Change book's status",
        "6": "Exit",
    }
    while True:
        for k, v in menu.items():
            print(f"{k}. {v}")
        choice = input("\nChouse options: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = input("Enter the year of publication of the book: ")
            library.add_book(title, author, year)
        elif choice == "2":
            book_id = input("Enter the book ID to delete: ")
            library.delete_book(book_id)
        elif choice == "3":
            search_field = input("Enter the search field: ")
            search_value = input("Enter a value to search for: ")
            library.search_book(search_field, search_value)
        elif choice == "4":
            library.get_all_books()
        elif choice == "5":
            book_id = input("Enter the book ID to change the status: ")
            new_status = input("Enter the new status of the book (in stock/given): ")
            library.change_status(book_id, new_status)
        elif choice == "6":
            break
        else:
            print("\nWrong choice, try again.")


if __name__ == "__main__":
    main()
