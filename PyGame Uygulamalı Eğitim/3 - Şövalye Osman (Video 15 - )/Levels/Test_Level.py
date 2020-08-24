import pygame
from Character.Character import Character
from Levels.materials import *


class TestLevel:
    def __init__(self, window_width, window_height):
        self.background = pygame.image.load("Levels/Level_Data/Test_Level/BackGroundTree.png").convert()
        self.background = pygame.transform.scale(self.background, (window_width, window_height))

        self.character = Character()
        self.coin_list = []
        self.coin_list.append(get_coin(600, 760))
        self.coin_list.append(get_coin(800, 760))
        self.coin_list.append(get_coin(1000, 760))

    def draw(self, window):
        window.blit(self.background, (0, 0))

        for coin in self.coin_list:
            window.blit(coin[0], (coin[1], coin[2]))
            # pygame.draw.rect(window, (0, 0, 255), (coin[1] + 18, coin[2] + 17, 25, 25), 2)

        self.character.draw(window)

    def game_loop(self, key, mouse):

        self.character.game_loop(key, mouse)

        for coin in self.coin_list:
            if (self.character.get_rect()).colliderect(coin[3]):
                self.character.gold += 100
                self.coin_list.remove(coin)

        if key[pygame.K_o]:
            return "Test_Level_Night"
