import pygame
from Character.Character import Character
from Levels.materials import *

class TestLevel:
    def __init__(self, windows_width, windows_height):
        # level things
        self.Test_BackGround = pygame.image.load("Levels/Level_Data/Test_Level/BackGroundTree.png").convert()
        self.Test_BackGround = pygame.transform.scale(self.Test_BackGround, (windows_width, windows_height))


        # cons
        self.Character = Character()
        self.coin_list = []

    def Draw(self,window):
        window.blit(self.Test_BackGround, (0, 0))

        for coin in self.coin_list:
            window.blit(coin[2], (coin[0], coin[1]))
            pygame.draw.rect(window, (0, 0, 255), (coin[0] + 15, coin[1] + 15, 30, 30), 3)

        self.Character.Draw(window)

    def GameLoop(self, Key, Mouse):

        self.control()

        self.Character.GameLoop(Key, Mouse)

        if Key[pygame.K_o]:
            return "Test_Level_Night"

    def control(self):
        for coin in self.coin_list:
            if (self.Character.get_rect()).colliderect(coin[3]):
                self.Character.gold += 100
                self.coin_list.remove(coin)
