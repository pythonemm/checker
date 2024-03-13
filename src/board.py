from src.piece import Piece, Color


class Board:
    def __init__(self):
        self._board = [
            ['-', Piece(Color('B')), '-', Piece(Color('B')), '-', Piece(Color('B')), '-', Piece(Color('B'))],
            [Piece(Color('B')), '-', Piece(Color('B')), '-', Piece(Color('B')), '-', Piece(Color('B')), '-'],
            ['-', Piece(Color('B')), '-', Piece(Color('B')), '-', Piece(Color('B')), '-', Piece(Color('B'))],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            [Piece(Color('W')), '-', Piece(Color('W')), '-', Piece(Color('W')), '-', Piece(Color('W')), '-'],
            ['-', Piece(Color('W')), '-', Piece(Color('W')), '-', Piece(Color('W')), '-', Piece(Color('W'))],
            [Piece(Color('W')), '-', Piece(Color('W')), '-', Piece(Color('W')), '-', Piece(Color('W')), '-']
        ]

    def get_board_as_table(self):
        pass