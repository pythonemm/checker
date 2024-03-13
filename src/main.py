from src.board import Board
from src.utils import draw_table

if __name__ == '__main__':
    board = Board()
    draw_table(board.get_board_as_table())
