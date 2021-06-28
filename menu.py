import sys
import pygame
from pygame.color import Color

from game import Game

FONT_GAME = 'assets/fonts/press_start.ttf'
COLOR_WHITE = Color('white')
COLOR_BLACK = Color('black')
WIDTH = 800
HEIGHT = 600


# noinspection PyMethodMayBeStatic
class Menu:
    def __init__(self, title):
        # screen
        self.screen_surface = pygame.display.set_mode(size=(WIDTH, HEIGHT))
        self.screen = pygame.display
        self.screen.set_caption(title)
        # mouse
        self.mouse_position = pygame.mouse.get_pos()
        # size screen
        self.width = WIDTH
        self.height = HEIGHT

        self.__is_in_menu = False

        self.size_start_text = 0
        self.text_screen = ''
        self.text_rect = ''
        self.game = Game()

    def __game_font(self, size):
        return pygame.font.Font(FONT_GAME, size)

    def __quit_game(self):
        pygame.quit()
        sys.exit()

    def __draw_text(self, btn, width, height, font_size=25):
        """Config quit button"""
        font = self.__game_font(size=font_size)
        quit_text = font.render(btn, True, COLOR_WHITE, COLOR_BLACK)
        quit_rect = quit_text.get_rect()
        quit_rect.center = (width, height)
        self.screen_surface.blit(quit_text, quit_rect)

    def __handle_click_button(self):
        is_clicked = pygame.mouse.get_pressed(num_buttons=3)
        if any(is_clicked):
            px, py = pygame.mouse.get_pos()
            if self.__is_in_menu:
                if 345 <= px <= 458:
                    if 213 <= py <= 247:
                        # print('Play')
                        self.__is_in_menu = False
                        self.__play_game()
                    elif 282 <= py <= 314:
                        self.__is_in_menu = False
                        self.__score()
                    elif 356 <= py <= 385:
                        self.__is_in_menu = False
                        self.__credits()
                    elif 422 <= py <= 453:
                        self.__quit_game()
            elif not self.__is_in_menu:
                if 10 <= px <= 80:
                    if 10 <= py <= 35:
                        self.show_menu_game_options()

    def __credits(self):
        self.screen_surface.fill(color=COLOR_BLACK)
        self.__draw_text('Back', 50, 30, font_size=15)
        self.__draw_text('Carlos Martins', WIDTH / 2, HEIGHT / 2 - 100)
        self.__draw_text('Dayvson Silva', WIDTH / 2, HEIGHT / 2 - 50)
        self.__draw_text('Elikson Tavares', WIDTH / 2, HEIGHT / 2)
        self.__draw_text('Fábio Ono', WIDTH / 2, HEIGHT / 2 + 50)
        self.__draw_text('Gustavo Fadel', WIDTH / 2, HEIGHT / 2 + 100)

    def __score(self):
        self.screen_surface.fill(color=COLOR_BLACK)
        self.__draw_text('Back', 50, 30, font_size=15)
        self.__draw_text('Carlos Martins\n'
                         'Dayvson Silva\n'
                         'Elikson Tavares\n'
                         'Fábio Ono\n'
                         'Gustavo Fadel', WIDTH / 2, HEIGHT / 2)

    def __play_game(self):
        self.game.game_loop()

    def __draw_game_name(self, name):
        """Define game name on start screen"""
        text = ''
        font = self.__game_font(size=60)
        for char in name:
            text += char
            text_screen = font.render(text, True, COLOR_WHITE, COLOR_BLACK)
            text_rect = text_screen.get_rect()
            text_rect.center = (self.width/2, (self.height/2)-200)
            self.screen_surface.blit(text_screen, text_rect)
            self.update()
            pygame.time.wait(300)

    def show_menu_game_options(self):
        self.screen_surface.fill(color=COLOR_BLACK)
        self.__is_in_menu = True
        self.__draw_game_name('ASTEROID')
        self.__draw_text('Play', WIDTH / 2, (HEIGHT / 2) - 70)
        self.__draw_text('Scores', WIDTH / 2, (HEIGHT / 2))
        self.__draw_text('Credits', WIDTH / 2, (HEIGHT / 2) + 70)
        self.__draw_text('Quit', WIDTH / 2, (HEIGHT / 2) + 140)

    def update(self):
        """Update screen"""
        self.screen.update()
        self.__handle_click_button()


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    s = Menu('Menu Game')
    s.show_menu_game_options()

    while True:
        handle_events()
        s.update()
        # s.draw_quit_button()
