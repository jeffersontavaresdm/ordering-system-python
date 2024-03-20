class EmailAlreadyExistsException(Exception):
    def __init__(self, message="Email already exists"):
        super().__init__(message)
