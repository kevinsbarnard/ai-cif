# board.py
# Board info

from graphics import *

SIDE_LENGTH = 50


class Board:
    cells = None
    n_cols = 0
    n_rows = 0

    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.cells = [[
            BoardCell(row, col, color='gray')
            if n_rows - 1 > row > 0 and n_cols - 1 > col > 0
            else BoardCell(row, col, color='black')
            for col in range(self.n_cols)]
            for row in range(self.n_rows)]

    def draw(self, win: GraphWin):
        for row in self.cells:
            for cell in row:
                cell.draw(win)

    def get_cell(self, row, col):
        return self.cells[row][col]

    def reset_color(self, color):
        for row in self.cells:
            for cell in row:
                if cell.color == color:
                    cell.set_color('gray')


class BoardCell:
    rect = None
    color = None
    row = 0
    col = 0

    def __init__(self, row, col, color=None):
        self.row = row
        self.col = col
        self.color = color
        self.rect = Rectangle(
            Point(col * SIDE_LENGTH, row * SIDE_LENGTH),
            Point((col + 1) * SIDE_LENGTH, (row + 1) * SIDE_LENGTH)
        )
        self.rect.setFill(color)

    def draw(self, win: GraphWin):
        self.rect.draw(win)

    def set_color(self, color: str):
        self.color = color
        self.rect.setFill(color)
