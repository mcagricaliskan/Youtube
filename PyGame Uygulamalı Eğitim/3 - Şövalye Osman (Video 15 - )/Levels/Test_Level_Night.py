import pygame
from Character.Character import Character


class TestLevelNight:
    def __init__(self, windows_width, windows_height):
        self.background = pygame.image.load("Levels/Level_Data/Test_Level_Night/Background.png").convert()
        self.background = pygame.transform.scale(self.background, (windows_width, windows_height))

        self.character = Character()

    def draw(self, window):
        window.blit(self.background, (0, 0))
        self.character.draw(window)

    def game_loop(self, key, mouse):

        self.character.game_loop(key, mouse)