import pygame
from sudoku_generator import SudokuGenerator


#reusable class for making buttons - Aaron
class Button:
    def __init__(self, x, y, width, height, text, color, text_color='black'):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont('Arial', 40)
        text_render = font.render(self.text, True, self.text_color)
        text_pos = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_pos)

    def button_click(self, pos):
        return self.rect.collidepoint(pos)


def draw_start(screen, buttons):
    screen.fill('white')
    for button in buttons:
        button.draw_button(screen)


# main game loop -Aaron

def main():
    pygame.init()
    screen = pygame.display.set_mode((750, 750))
    pygame.display.set_caption('Sudoku!')

    state = 'start'

    easy_button = Button(150,450,100,50, 'Easy', "green")
    medium_button = Button(312.5, 450, 125, 50, 'Medium', "orange")
    hard_button = Button(500, 450, 100, 50, 'Hard', "red")
    start_buttons = [easy_button, medium_button, hard_button]



    board = None
    playing = True
    while playing:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
            if state == 'start':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y =  event.pos
                pass
            elif state == 'playing':
                pass

        if state == 'start':
            draw_start(screen, start_buttons)
        elif state == 'playing':
            screen.fill('blue')
        pygame.display.update()



if __name__ == '__main__':
    main()