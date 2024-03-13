from src.piece import Piece, Color


class Board:
    def __init__(self, board: list[list[Piece | None]]) -> None:
        self._board = board

    def get_board_as_table(self):
        pass
