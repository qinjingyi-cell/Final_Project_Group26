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

        self.solution = copy.deepcopy(self.sudoku_generator.get_board())
        self.sudoku_generator.remove_cells()

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
    Toggle .selected attribute of the given Cell if it has no value.
    '''
    def select(self, row, col):
        self.selected = self.cells[col][row]
        print(self.selected)
        if self.selected.value == 0:
            if self.selected.selected == False:
                self.selected.selected = True
            elif self.selected.selected == True:
                self.selected.selected = False
                self.selected = None

    '''
    When click
    input: x-position and y-position and output: row and col if it is between the displayed board (630x630)
    '''
    def click(self, x, y):  
        ordered_pair = (x//70,y//70)
        return ordered_pair if all(coord < 9 for coord in ordered_pair) else None


    def clear(self):
        ### Clear sketched value
        if self.selected:
            self.selected.sketched_value = None


    def sketch(self, value):
        self.selected.sketched_value = value


    def place_number(self, value):
        pass


    def reset_to_original(self):
        pass


    def is_full(self):
        pass


    def update_board(self):
        pass


    def find_empty(self):
        pass


    def check_board(self):
        pass

