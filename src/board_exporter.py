import csv

from src.board import Board
from src.board_factory import BoardFactory


class BoardExporter:
    def export_board(self, board: Board, filename: str) -> None:
        board_as_table = board.get_board()
        board_as_str = []

        for row in board_as_table:
            board_line = []
            for piece in row:
                if piece:
                    board_line.append(str(piece))
                else:
                    board_line.append('')
            board_as_str.append(board_line)

        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(board_as_str)


if __name__ == "__main__":
    file = '../initial_board.csv'
    board = BoardFactory().build_from_csv(file)

    exporter = BoardExporter()
    exporter.export_board(board, '../game_1')
