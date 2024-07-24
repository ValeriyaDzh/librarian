from datetime import datetime
from uuid import uuid1


class Book:

    def __init__(self, title: str, author: str, year: str) -> None:
        self.id = self._generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    @staticmethod
    def _generate_id() -> str:
        """
        Function for creating a unique ID
        """
        unique_id = str(uuid1())[:8]
        current_date = datetime.today().date().isoformat()
        return f"{unique_id}-{current_date}"
