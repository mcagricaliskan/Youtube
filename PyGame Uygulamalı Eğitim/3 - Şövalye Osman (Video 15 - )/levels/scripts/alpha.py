import pygame
from character.character import *
from levels.scripts.map import *


class Alpha:
    def __init__(self, window_width, window_height, level_name):

        self.level_name = level_name
        self.map = Map(self.level_name)

        self.character = Character()

    def draw(self, window):
        window.fill((125, 125, 125))
        self.map.draw_map(window)
        self.character.draw(window)

    def game_loop(self, key, mouse):

        self.character.game_loop(key, mouse)
