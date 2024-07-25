import json
import os
import unittest
from app.file_helpers import save, load_data


class TestFileHelpers(unittest.TestCase):

    def test_save_and_load_data(self):
        data = {"test1": 1, "name": 2}
        file_path = "test.json"

        save(data, file_path)

        with open(file_path, encoding="utf-8") as file:
            file_data = json.load(file)
            self.assertEqual(
                [data],
                file_data["books"],
                "Data saved in file doesn't match the expected data.",
            )

        loaded_data = load_data(file_path)
        self.assertEqual(
            [data],
            loaded_data["books"],
            "Data loaded from file doesn't match the expected data.",
        )

        os.remove(file_path)

    def test_load_data_file_not_exist(self):
        fake_file_path = "fake_file.json"

        loaded_data = load_data(fake_file_path)
        self.assertEqual(
            loaded_data,
            {"books": []},
            "Expected empty list for 'books' when file doesn't exist.",
        )


if __name__ == "__main__":
    unittest.main()
