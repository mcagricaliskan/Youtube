import pygame
from Character.Character import Character

class TestLevel:
    def __init__(self, windows_width, windows_height):
        self.Test_BackGround = pygame.image.load("Levels/Level_Data/Test_Level/BackGroundTree.png").convert()
        self.Test_BackGround = pygame.transform.scale(self.Test_BackGround, (windows_width, windows_height))

        self.Character = Character()

    def Draw(self,window):
        window.blit(self.Test_BackGround, (0, 0))
        self.Character.Draw(window)


    def GameLoop(self):

        self.Character.GameLoop()