import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        if self.value == 0:
            self.sketched_value = 0
        else:
            self.sketched_value = None
        self.selected = False


    def set_cell_value(self, value):
        self.value = value
        self.sketched_value = 0


    def set_sketched_value(self, value):
        self.sketched_value = value


    def draw(self):
        cell_size = 70
        x = self.col * cell_size
        y = self.row * cell_size

        final_font = pygame.font.SysFont('consolas', 40)
        sketch_font = pygame.font.SysFont('consolas', 30)
        if self.sketched_value is not None:
            # Interactable color (lighter)
            pygame.draw.rect(self.screen, (185, 220, 235), (x, y, cell_size, cell_size))
        if self.selected:
            # Selected color (darker)
            pygame.draw.rect(self.screen, pygame.Color(140, 190, 210), (x, y, cell_size, cell_size))
        if self.value != 0:             
            # Cell number
            number = final_font.render(str(self.value), True, (255, 255, 255))
            num_pos = number.get_rect(midbottom=(x + cell_size//2, y + cell_size))

            self.screen.blit(number, num_pos)
        
        elif self.sketched_value is not None and self.sketched_value != 0:       # Shows cell sketched value at the tope left
            number = sketch_font.render(str(self.sketched_value), True, (255, 255, 255))
            num_pos = number.get_rect(center=(x + cell_size//4, y + cell_size//3))

            self.screen.blit(number, num_pos)

        
    
    def __str__(self):
        return f"{self.value} at ({self.col},{self.row})"