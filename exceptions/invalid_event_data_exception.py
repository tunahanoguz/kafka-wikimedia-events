class InvalidEventDataException(Exception):
    def __init__(self):
        super().__init__(f"Event data is invalid!")
