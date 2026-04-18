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

        self.original_board = SudokuGenerator(9, self.removed_cell)
        self.board = SudokuGenerator(9, self.removed_cell)



    def draw(self):
        for i in range(10):
            pygame.draw.line(self.screen, "black", (i*80, 0), (i*80,720), 4)
        for i in range(10):
            pygame.draw.line(self.screen, "black", (0, i * 80), (720, i*80), 4)


    def select(self, row, col):
        pass


    def click(self, x, y):
        pass


    def clear(self):
        pass


    def sketch(self, value):
        pass


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

