import tkinter as tk
from src.board_factory import BoardFactory
from src.piece import Color


class CheckerboardUI:
    PIECE_RADIUS = 20
    SELECTED_COLOR = "#FF0000"
    DARK_COLOR = "#5D432C"
    LIGHT_COLOR = "#FFE8D6"
    SQUARE_SIZE = 50
    last_square_clicked = None

    def __init__(self, master, board):
        self.master = master
        self.board = board
        self.master.title("Checkerboard")

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.draw_board()
        self.last_square_clicked = None
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                x1 = col * self.SQUARE_SIZE
                y1 = row * self.SQUARE_SIZE
                x2 = x1 + self.SQUARE_SIZE
                y2 = y1 + self.SQUARE_SIZE

                if self.last_square_clicked == (row, col):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.SELECTED_COLOR, outline='')
                elif (row + col) % 2 == 0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.LIGHT_COLOR, outline='')
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.DARK_COLOR, outline='')

        self.draw_pieces()

    def draw_pieces(self):
        for row_index, row in enumerate(self.board.get_board()):
            for col_index, piece in enumerate(row):
                if piece:
                    x = col_index * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
                    y = row_index * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
                    color = "black" if piece.color == Color.BLACK else "white"
                    self.canvas.create_oval(x - self.PIECE_RADIUS, y - self.PIECE_RADIUS,
                                            x + self.PIECE_RADIUS, y + self.PIECE_RADIUS, fill=color)
                    if piece.is_queen:
                        self.canvas.create_text(x, y, text="Q", fill="red", font=('Arial','15','bold'))

    def handle_click(self, event):
        col = event.x // self.SQUARE_SIZE
        row = event.y // self.SQUARE_SIZE
        clicked_position = (row, col)

        if clicked_position == self.last_square_clicked:
            self.last_square_clicked = None
        else:
            if self.last_square_clicked:
                print(f'move from {self.last_square_clicked[0]} to {clicked_position}')
                self.board.move(self.last_square_clicked, clicked_position)
                self.last_square_clicked = None
            else:
                self.last_square_clicked = clicked_position

        self.canvas.delete("all")
        self.draw_board()


if __name__ == "__main__":
    file = '../initial_board.csv'
    board = BoardFactory().build_from_csv(file)

    root = tk.Tk()
    app = CheckerboardUI(root, board)
    root.mainloop()
