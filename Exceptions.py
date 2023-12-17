class EmptyBoardException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'ERROR ' + self.message

class FullBoardException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'ERROR ' + self.message

class NoSuchDominoException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'ERROR ' + self.message

class InvalidNumberException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'ERROR ' + self.message
