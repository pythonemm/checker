from src.piece import Piece, Color
from src.utils import draw_table


class Board:
    def __init__(self, board: list[list[Piece | None]]) -> None:
        self._board = board

    def move(self, from_position: tuple[int, int], to_position: tuple[int, int]) -> None:
        ...
        #   TODO

    def get_board(self) -> list[list[Piece]]:
        return self._board

    def get_piece(self, position: tuple[int]) -> Piece | None:
        return self._board[position[0]][position[1]]

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
