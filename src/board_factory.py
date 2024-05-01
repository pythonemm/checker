from src.board import Board
from src.exeptions import GameError
from src.piece import Piece, Color


class PieceFactory:
    @staticmethod
    def build_from_string(string: str) -> Piece | None:
        if any(string == member.value for member in Color):
            return Piece(Color(string))
        elif string == '':
            return None
        else:
            raise GameError('Invalid Piece')


class BoardFactory:
    @staticmethod
    def build_from_csv(csv_file: str):
        table = [line.strip().split(',') for line in open(csv_file)]
        board = []

        for row in table:
            board_row = []
            for element in row:
                piece = PieceFactory.build_from_string(element)
                board_row.append(piece)
            board.append(board_row)
        return Board(board)

if __name__ == '__main__':
    file = '../initial_board.csv'
    board = BoardFactory().build_from_csv(file)
    print(board)
