"""
An Error Class so I can write my own errors
"""

class FastqFormatError(Exception):
    """
    Exception raised for sequences not being paired properly.

    :param message: explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ColorNotFoundError(Exception):
    """
    Exception raised for a color not being found.

    :param message: explanation of the error
    """

    def __init__(self, message):
        self.message = message
