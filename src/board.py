from src.piece import Piece, Color
from src.utils import draw_table


class Board:
    def __init__(self, board: list[list[Piece | None]]) -> None:
        self._board = board

    def draw(self) -> None:
        board = []
        for row_index, row in enumerate(self._board):
            row_as_str = []
            for column_index, piece in enumerate(row):
                if piece:
                    row_as_str.append(str(piece))
                elif (column_index + row_index) % 2 == 1:
                    row_as_str.append('#')
                else:
                    row_as_str.append('')
            board.append(row_as_str)

        draw_table(board)
