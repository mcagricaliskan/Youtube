import pygame
from Character.Character import Character
from Levels.materials import *

class TestLevel:
    def __init__(self, windows_width, windows_height):
        self.Test_BackGround = pygame.image.load("Levels/Level_Data/Test_Level/BackGroundTree.png").convert()
        self.Test_BackGround = pygame.transform.scale(self.Test_BackGround, (windows_width, windows_height))

        self.Character = Character()
        self.coin_list = []
        self.coin_list.append(get_coin(600, 760))
        self.coin_list.append(get_coin(800, 760))
        self.coin_list.append(get_coin(1000, 760))

    def Draw(self,window):
        window.blit(self.Test_BackGround, (0, 0))

        for coin in self.coin_list:
            window.blit(coin[0], (coin[1], coin[2]))
            #pygame.draw.rect(window, (0, 0, 255), (coin[1] + 18, coin[2] + 17, 25, 25), 2)

        self.Character.draw(window)



    def GameLoop(self, Key, Mouse):

        self.Character.game_loop(Key, Mouse)
        print(self.Character.gold)

        for coin in self.coin_list:
            if (self.Character.get_rect()).colliderect(coin[3]):
                self.Character.gold += 100
                self.coin_list.remove(coin)

        if Key[pygame.K_o]:
            return "Test_Level_Night"