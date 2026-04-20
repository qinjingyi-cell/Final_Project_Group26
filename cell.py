import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None
        self.selected = False


    def set_cell_value(self, value):
        self.value = value
        self.sketched_value = None


    def set_sketched_value(self, value):
        self.sketched_value = value


    def draw(self):
        cell_size = 70
        x = self.col * cell_size
        y = self.row * cell_size

        final_font = pygame.font.SysFont('Georgia', 40)
        sketch_font = pygame.font.SysFont('Georgia', 30)

        if self.value != 0:
            number = final_font.render(str(self.value), True, (255, 255, 255))
            num_pos = number.get_rect(center=(x + cell_size//2, y + cell_size//2))

            self.screen.blit(number, num_pos)

        elif self.sketched_value is not None:       # Shows cell sketched value at the tope left
            number = sketch_font.render(str(self.sketched_value), True, (255, 255, 255))
            num_pos = number.get_rect(center=(x + cell_size//4, y + cell_size//4))

            self.screen.blit(number, num_pos)

        if self.selected:
            pygame.draw.rect(self.screen, (100, 160, 200), (x+1, y+1, cell_size, cell_size), 3)
    
    def __str__(self):
        return f"{self.value} at ({self.col},{self.row})"