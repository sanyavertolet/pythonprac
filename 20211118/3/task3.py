import string

class Alpha:
    __slots__ = [*string.ascii_lowercase]
    def __init__(self, **kwargs):
        for letter, value in kwargs.items():
            setattr(self, letter, value)

    def __str__(self):
        return ', '.join([f'{ letter }: { getattr(self, letter) }' for letter in string.ascii_lowercase if hasattr(self, letter)])

class AlphaQ:
    def __init__(self, **kwargs):
        for letter, value in kwargs.items():
            if letter in string.ascii_lowercase:
                setattr(self, letter, value)
            else:
                raise AttributeError()

    def __setattr__(self, obj, val):
        if obj in string.ascii_lowercase:
            super().__setattr__(obj, val)
        else:
            raise AttributeError()

    def __str__(self):
        return ', '.join([f'{ letter }: { getattr(self, letter) }' for letter in string.ascii_lowercase if hasattr(self, letter)])

import sys
exec(sys.stdin.read())
