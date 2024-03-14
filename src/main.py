from src.board_factory import BoardFactory

if __name__ == '__main__':
    file = '../initial_board.csv'
    board = BoardFactory().build_from_csv(file)
    board.draw()
