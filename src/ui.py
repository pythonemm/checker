import tkinter as tk
from tkinter import Menu, filedialog
from src.board_exporter import BoardExporter
from src.board_factory import BoardFactory
from src.piece import Color


class CheckerboardUI:
    SQUARE_SIZE = 50
    PIECE_RADIUS = 20
    SELECTED_COLOR = "#FF0000"
    DARK_COLOR = "#5D432C"
    LIGHT_COLOR = "#FFE8D6"
    INITIAL_BOARD_FILE = '../initial_board.csv'
    DEFAULT_EXPORT_FOLDER = '../saved_games'

    def __init__(self, master):
        self.master = master
        self.board = BoardFactory().build_from_csv(self.INITIAL_BOARD_FILE)
        self.last_square_clicked = None
        self.master.title("Checkerboard")

        self.create_menu()

        self.canvas = tk.Canvas(master, width=8 * self.SQUARE_SIZE, height=8 * self.SQUARE_SIZE)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)

    def create_menu(self):
        menubar = Menu(self.master)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Import Board", command=self.import_board)
        file_menu.add_command(label="Export Board", command=self.export_board)
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_command(label="Skip turn")
        self.master.config(menu=menubar)

    def draw_board(self):
        self.canvas.delete("all")
        if self.board:
            for row in range(8):
                for col in range(8):
                    x1, y1 = col * self.SQUARE_SIZE, row * self.SQUARE_SIZE
                    x2, y2 = x1 + self.SQUARE_SIZE, y1 + self.SQUARE_SIZE
                    fill_color = self.LIGHT_COLOR if (row + col) % 2 == 0 else self.DARK_COLOR
                    if self.last_square_clicked == (row, col):
                        fill_color = self.SELECTED_COLOR
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline='')

            self.draw_pieces()

    def draw_pieces(self):
        for row_index, row in enumerate(self.board.get_board()):
            for col_index, piece in enumerate(row):
                if piece:
                    x, y = col_index * self.SQUARE_SIZE + self.SQUARE_SIZE // 2, row_index * self.SQUARE_SIZE + self.SQUARE_SIZE // 2
                    color = "black" if piece.color == Color.BLACK else "white"
                    self.canvas.create_oval(x - self.PIECE_RADIUS, y - self.PIECE_RADIUS,
                                            x + self.PIECE_RADIUS, y + self.PIECE_RADIUS, fill=color)
                    if piece.is_queen:
                        self.canvas.create_text(x, y, text="Q", fill="red", font=('Arial', '15', 'bold'))

    def handle_click(self, event):
        if self.board:
            col, row = event.x // self.SQUARE_SIZE, event.y // self.SQUARE_SIZE
            clicked_position = (row, col)

            if clicked_position == self.last_square_clicked:
                self.last_square_clicked = None
            else:
                if self.last_square_clicked:
                    self.board.move(self.last_square_clicked, clicked_position)
                    self.last_square_clicked = None
                else:
                    self.last_square_clicked = clicked_position

            self.draw_board()

    def import_board(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.board = BoardFactory().build_from_csv(file_path)
            self.draw_board()

    def export_board(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")],
                                                  initialdir=self.DEFAULT_EXPORT_FOLDER)
        if file_path:
            exporter = BoardExporter()
            exporter.export_board(self.board, file_path)
