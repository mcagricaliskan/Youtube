import pygame
from Character.Character import Character

class TestLevelNight:
    def __init__(self, windows_width, windows_height):
        self.Test_BackGround = pygame.image.load("Levels/Level_Data/Test_Level_Night/Background.png").convert()
        self.Test_BackGround = pygame.transform.scale(self.Test_BackGround, (windows_width, windows_height))

        self.Character = Character()

    def Draw(self,window):
        window.blit(self.Test_BackGround, (0, 0))
        self.Character.draw(window)

    def GameLoop(self, Key, Mouse):

        self.Character.game_loop(Key, Mouse)