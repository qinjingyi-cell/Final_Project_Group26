import pygame
import sys
from board import Board


#reusable class for making buttons - Aaron
class Button:
    def __init__(self, x, y, width, height, text, color, text_color='white'):
        self.rect = pygame.Rect(x, y, width, height)
        self.back_rect = pygame.Rect(x-5,y-5,width+5,height+5)
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw_button(self, screen):
        pygame.draw.rect(screen, (129, 188, 214), self.back_rect)
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont('Georgia', 35)
        text_render = font.render(self.text, True, self.text_color)
        text_pos = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_pos)

    def button_click(self, pos):
        return self.rect.collidepoint(pos)

#functions

def draw_start(screen, buttons):
    screen.fill('light blue')

    font = pygame.font.SysFont('Georgia', 40)
    title = font.render('Welcome to Sudoku!', True, 'white')
    difficulty_text = font.render('Select Game Mode:', True, 'white')

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

    easy_button = Button(107.5,450,100,50, 'Easy', (110, 220, 80))
    medium_button = Button(237.5, 450, 155, 50, 'Medium', "orange")
    hard_button = Button(422.5, 450, 100, 50, 'Hard', (220, 70, 70))
    start_buttons = [easy_button, medium_button, hard_button]

    reset_button = Button(50, 655, 110, 50, 'Reset', (60, 80, 180))
    restart_button = Button(240, 655, 150, 50, 'Restart', (110, 220, 80))
    exit_button = Button(480, 655, 100, 50, 'Exit', (220, 70, 70))
    in_game_buttons = [reset_button, restart_button, exit_button]

    board = None
    '''
    Cells and board are between a 630x630 square. (Total window 630x730)
    '''
    playing = True
    selection = False
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if state == 'start':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.button_click(event.pos):
                        board = Board(630, 730, screen, 'easy')
                        state = 'playing'
                    elif medium_button.button_click(event.pos):
                        board = Board(630, 730, screen, 'medium')
                        state = 'playing'
                    elif hard_button.button_click(event.pos):
                        board = Board(630, 730, screen, 'hard')
                        state = 'playing'
            elif state == 'playing':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.button_click(event.pos):
                        pygame.quit()
                        sys.exit()
                    if restart_button.button_click(event.pos):
                        state = 'start'
                    if reset_button.button_click(event.pos):
                        board.reset_to_original()
                    else:
                        if selection:
                            board.select(position[0],position[1])   # deselects previous cell
                        x,y = event.pos
                        position = board.click(x,y)                 # returns ordered_pair (x,y) [tuple] if the click is inside the board, else returns None
                        if position:
                            board.select(position[0],position[1])
                            selection = True
                        else:
                            selection = False
                        sketched_value = None
                if event.type == pygame.KEYDOWN and selection:
                    ### Sketch values (when 1-9 is pressed)
                    key_name = pygame.key.name(event.key).strip("[]")
                    if key_name.isdigit() and key_name != "0":
                        number = int(key_name)
                        board.sketch(number)
                        sketched_value = number
                    ### Clear selected cell (When backspace is pressed)
                    elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        board.clear()
                    ### If there is a sketched value it will place it
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        try:
                            board.place_number(sketched_value)
                        except UnboundLocalError:
                            continue
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