from enum import Enum


class Color(Enum):
    WHITE = 'W'
    BLACK = 'B'


class Piece:
    def __init__(self, color: Color):
        self.color = color
