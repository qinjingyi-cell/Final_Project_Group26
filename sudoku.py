import pygame
from board import Board


#reusable class for making buttons - Aaron
class Button:
    def __init__(self, x, y, width, height, text, color, text_color='black'):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont('Georgia', 40)
        text_render = font.render(self.text, True, self.text_color)
        text_pos = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_pos)

    def button_click(self, pos):
        return self.rect.collidepoint(pos)

#funtions

def draw_start(screen, buttons):
    screen.fill('white')

    font = pygame.font.SysFont('Georgia', 40)
    title = font.render('Welcome to Sudoku!', True, 'black')
    difficulty_text = font.render('Select Game Mode:', True, 'black')

    screen_width = screen.get_width()
    title_pos = title.get_rect(center=(screen_width/2, 146))
    diff_text_pos = difficulty_text.get_rect(center=(screen_width/2, 365))
    screen.blit(title, title_pos)
    screen.blit(difficulty_text, diff_text_pos)

    for button in buttons:
        button.draw_button(screen)


# main game loop -Aaron

def main():
    pygame.init()
    screen = pygame.display.set_mode((630, 730))
    pygame.display.set_caption('Sudoku!')

    state = 'start'

    easy_button = Button(107.5,450,100,50, 'Easy', "green")
    medium_button = Button(237.5, 450, 155, 50, 'Medium', "orange")
    hard_button = Button(422.5, 450, 100, 50, 'Hard', "red")
    start_buttons = [easy_button, medium_button, hard_button]

    reset_button = Button(50, 655, 110, 50, 'Reset', 'blue')
    restart_button = Button(240, 655, 150, 50, 'Restart', 'green')
    exit_button = Button(480, 655, 100, 50, 'Exit', 'red')
    in_game_buttons = [reset_button, restart_button, exit_button]


    board = None
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if state == 'start':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.button_click(event.pos):
                        board = Board(630,730, screen, 'easy')
                        state = 'playing'
                    elif medium_button.button_click(event.pos):
                        board = Board(630,730, screen, 'medium')
                        state = 'playing'
                    elif hard_button.button_click(event.pos):
                        board = Board(630, 730, screen, 'hard')
                        state = 'playing'
            elif state == 'playing':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.button_click(event.pos):
                        pygame.quit()

        if state == 'start':
            draw_start(screen, start_buttons)
        elif state == 'playing':
            screen.fill('light blue')
            board.draw()
            for button in in_game_buttons:
                button.draw_button(screen)


        pygame.display.update()



if __name__ == '__main__':
    main()