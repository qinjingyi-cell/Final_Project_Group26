import copy

import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        if difficulty == 'easy':
            self.removed_cell = 30
        elif difficulty == 'medium':
            self.removed_cell = 40
        else:
            self.removed_cell = 50

        self.sudoku_generator = SudokuGenerator(9, self.removed_cell)
        self.sudoku_generator.fill_values()

        
        self.sudoku_generator.remove_cells()
        self.solution = copy.deepcopy(self.sudoku_generator.get_board())

        self.board = self.sudoku_generator.get_board()
        self.original_board = copy.deepcopy(self.board)

        self.cells = [
            [Cell(self.board[i][j], i, j, screen) for j in range(9)]
            for i in range(9)
        ]

        self.selected = None

    def draw(self):

        for i in range(10):             # draw grid
            if i % 3 == 0:
                line_width = 4
            else:
                line_width = 2

            pygame.draw.line(self.screen, "white", (i*70, 0), (i*70,630), line_width)
            pygame.draw.line(self.screen, "white", (0, i * 70), (630, i*70), line_width)

        for row in self.cells:          # draw cells (cell class function)
            for cell in row:
                cell.draw()

    '''
    Toggle .selected attribute of the given Cell if it is originally empty.
    And updates .selected attribute of board to cell.
    '''
    def select(self, row, col):
        if self.selected:
            self.selected.selected = False

        if self.original_board[col][row] == 0:
            self.selected = self.cells[col][row]
            self.selected.selected = True
        else:
            self.selected = None

    '''
    When click
    input: x-position and y-position and output: row and col if it is between the displayed board (630x630)
    '''
    def click(self, x, y):  
        ordered_pair = (x//70,y//70)
        return ordered_pair if all(coord < 9 for coord in ordered_pair) else None

    '''
    Clear sketched value of the selected cell.
    '''
    def clear(self):
        if self.selected:
            self.selected.value = 0
            self.selected.sketched_value = None


    def sketch(self, value):
        try:
            self.selected.set_sketched_value(value)
        except:
            pass


    def place_number(self, value):
        try:
            assert value != None
            self.selected.set_cell_value(value)
        except:
            pass


    def reset_to_original(self):
        self.board = self.original_board
        self.update_board()
        self.draw()


    def is_full(self):
        pass


    def update_board(self):
        self.cells = [
            [Cell(self.board[i][j], i, j, self.screen) for j in range(9)]
            for i in range(9)
        ]


    def find_empty(self):
        pass


    def check_board(self):
        pass
