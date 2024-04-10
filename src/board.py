from src.piece import Piece, Color
from src.utils import draw_table


class Board:
    def __init__(self, board: list[list[Piece | None]]) -> None:
        self._board = board

    def move(self, from_position: tuple[int, int], to_position: tuple[int, int]) -> None:
        piece = self._board[from_position[0]][from_position[1]]
        to_position_value = self._board[to_position[0]][to_position[1]]
        if piece and not to_position_value and self.is_valid_move(from_position, to_position):
            self._board[to_position[0]][to_position[1]] = piece
            self._board[from_position[0]][from_position[1]] = None

    def is_valid_move(self, from_position: tuple[int, int], to_position: tuple[int, int]) -> bool:
        piece = self._board[from_position[0]][from_position[1]]
        if piece.color == Color.BLACK:
            if from_position[0] - 1 == to_position[0]:
                if abs(from_position[1] - to_position[1]) == 1:
                    return True

        elif piece.color == Color.WHITE:
            if from_position[0] + 1 == to_position[0]:
                if abs(from_position[1] - to_position[1]) == 1:
                    return True

        return False

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
