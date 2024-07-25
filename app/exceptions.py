class NotFoundException(Exception):

    def __init__(self, message="\nThe book was not found"):
        super().__init__(message)


class InvalidFieldException(Exception):

    def __init__(
        self,
        message="\nAcceptable fields: id, author, title, year, status",
    ):
        super().__init__(message)


class InvalidStatusException(Exception):

    def __init__(
        self,
        message="\nAcceptable: in stock, given",
    ):
        super().__init__(message)
