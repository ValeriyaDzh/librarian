import unittest
from unittest.mock import patch
from app.exceptions import (
    NotFoundException,
    InvalidFieldException,
    InvalidStatusException,
)
from app.library_manager import Librarian


class MockedLibraryDatabase:
    def save_book(self, book: dict[str, str]):
        return book

    def load_books(self):
        return {
            "books": [
                {
                    "id": "a7d9edfa-2024-07-25",
                    "title": "test1",
                    "author": "Jone",
                    "year": "1889",
                    "status": "in stock",
                },
                {
                    "id": "a0b3542e-2024-07-25",
                    "title": "test2",
                    "author": "Arthur",
                    "year": "1998",
                    "status": "in stock",
                },
                {
                    "id": "cf863faa-2024-07-25",
                    "title": "test3",
                    "author": "Kate",
                    "year": "1678",
                    "status": "in stock",
                },
            ]
        }

    def update_books(self, books: dict[str, str]):
        return "updated"


class TestLibrarian(unittest.TestCase):
    def setUp(self) -> None:
        self.mocked_db = MockedLibraryDatabase()
        self.patcher = patch(
            "app.library_manager.LibraryDatabase", return_value=self.mocked_db
        )
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_add_book(self):
        librarian = Librarian()
        result = librarian.add_book("Test Book", "Author", "2023")
        self.assertEqual(result["title"], "Test Book")
        self.assertEqual(result["author"], "Author")
        self.assertEqual(result["year"], "2023")
        self.assertEqual(result["status"], "in stock")

    def test_search_book(self):
        librarian = Librarian()
        test_cases = [("title", "test1"), ("author", "Anna"), ("yeAr", "1889")]

        for search_by, search_value in test_cases:
            with self.subTest(search_by=search_by, search_value=search_value):
                librarian.search_book(search_by, search_value)

    def test_search_exceptions(self):
        librarian = Librarian()
        test_cases = [
            ("title", "T", NotFoundException),
            ("a", "Anna", InvalidFieldException),
        ]

        for search_by, search_value, serch_exception in test_cases:
            with self.subTest(
                search_by=search_by,
                search_value=search_value,
                serch_exception=serch_exception,
            ):
                librarian.search_book(search_by, search_value)
                self.assertRaises(serch_exception)

    def test_get_all_books(self):
        librarian = Librarian()
        result = librarian.get_all_books()
        self.assertEqual(
            result,
            [
                {
                    "id": "a7d9edfa-2024-07-25",
                    "title": "test1",
                    "author": "Jone",
                    "year": "1889",
                    "status": "in stock",
                },
                {
                    "id": "a0b3542e-2024-07-25",
                    "title": "test2",
                    "author": "Arthur",
                    "year": "1998",
                    "status": "in stock",
                },
                {
                    "id": "cf863faa-2024-07-25",
                    "title": "test3",
                    "author": "Kate",
                    "year": "1678",
                    "status": "in stock",
                },
            ],
        )

    def test_change_status(self):
        librarian = Librarian()
        result = librarian.change_status("a7d9edfa-2024-07-25", "given")

    def test_change_status_exceptions(self):
        librarian = Librarian()
        test_cases = [
            ("aaa", "given", NotFoundException),
            ("a7d9edfa-2024-07-25", "deleted", InvalidStatusException),
        ]

        for id, status, status_exception in test_cases:
            with self.subTest(id=id, status=status, status_exception=status_exception):
                librarian.change_status(id, status)
                self.assertRaises(status_exception)

    def test_delete_book(self):
        librarian = Librarian()
        result = librarian.delete_book("a7d9edfa-2024-07-25")
        self.assertEqual(result, "a7d9edfa-2024-07-25")

    def test_delete_non_existent_book(self):
        librarian = Librarian()
        librarian.delete_book("a7d9edfa-2024-07-29")
        self.assertRaises(NotFoundException)


if __name__ == "__main__":
    unittest.main()
