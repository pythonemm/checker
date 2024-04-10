from enum import Enum
from typing import Self


class Color(Enum):
    WHITE = 'W'
    BLACK = 'B'

    def swap(self) -> Self:
        if self is Color.WHITE:
            return Color.BLACK
        else:
            return Color.WHITE


class Piece:
    def __init__(self, color: Color):
        self.color = color
        self.is_queen = False

    def __len__(self):
        return 1

    def __str__(self):
        return str(self.color.value)
