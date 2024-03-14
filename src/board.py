from src.piece import Piece, Color
from src.utils import draw_table


class Board:
    def __init__(self, board: list[list[Piece | None]]) -> None:
        self._board = board

    def draw(self) -> None:
        board = []
        for row in self._board:
            row_as_str = [str(piece) if piece else '' for piece in row]
            board.append(row_as_str)

        draw_table(board)
