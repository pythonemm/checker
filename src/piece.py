from enum import Enum


class Color(Enum):
    WHITE = 'W'
    BLACK = 'B'


class Piece:
    def __init__(self, color: Color):
        self.color = color

    def __len__(self):
        return 1

    def __str__(self):
        return str(self.color.value)
