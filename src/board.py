from src.piece import Piece, Color
from src.utils import draw_table


class Board:
    def __init__(self, board: list[list[Piece | None]]) -> None:
        self._board = board
        self.player_turn = Color.WHITE

    def move(self, from_position: tuple[int, int], to_position: tuple[int, int]) -> None:
        piece = self._board[from_position[0]][from_position[1]]

        is_valid_move, as_captured = self.is_valid_move_and_capture(from_position, to_position)
        if is_valid_move:
            self._move(from_position, to_position, as_captured)
            if to_position[0] in {0, 7}:
                piece.is_queen = True

    def _move(self, from_position: tuple[int, int], to_position: tuple[int, int], as_captured: bool) -> None:
        piece = self._board[from_position[0]][from_position[1]]
        self._board[to_position[0]][to_position[1]] = piece
        self._board[from_position[0]][from_position[1]] = None

        if as_captured:
            capture_piece_col, capture_piece_row = self.get_middle_piece(from_position, to_position)
            self._board[capture_piece_row][capture_piece_col] = None
        self.player_turn = self.player_turn.swap()

    def is_valid_move_and_capture(self, from_position: tuple[int, int], to_position: tuple[int, int]) -> (bool, bool):
        piece = self._board[from_position[0]][from_position[1]]
        if not piece or self._board[to_position[0]][to_position[1]]:
            return False, False
        color = piece.color

        # If it's not the player's turn or the destination is occupied
        if color is not self.player_turn or self._board[to_position[0]][to_position[1]] is not None:
            return False, False

        row_diff = to_position[0] - from_position[0]
        col_diff = abs(to_position[1] - from_position[1])

        if (color == Color.BLACK or piece.is_queen) and row_diff == -1 and col_diff == 1:
            return True, False
        elif (color == Color.WHITE or piece.is_queen) and row_diff == 1 and col_diff == 1:
            return True, False
        elif abs(row_diff) == 2 and col_diff == 2:
            capture_piece_col, capture_piece_row = self.get_middle_piece(from_position, to_position)
            capture_piece = self._board[capture_piece_row][capture_piece_col]
            if capture_piece and capture_piece.color is not self.player_turn:
                return True, True

        return False, False

    def get_middle_piece(self, from_position, to_position):
        capture_piece_row = (from_position[0] + to_position[0]) // 2
        capture_piece_col = (from_position[1] + to_position[1]) // 2
        return capture_piece_col, capture_piece_row

    def get_board(self) -> list[list[Piece]]:
        return self._board

    def get_piece(self, position: tuple[int]) -> Piece | None:
        return self._board[position[0]][position[1]]
