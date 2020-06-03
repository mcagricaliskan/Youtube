import pygame
import sys
sys.path.append("/")
from Levels.Test_Level import TestLevel

pygame.init()

class GameCore:
    def __init__(self):
        self.windows_width = 1600
        self.windows_height = 900
        self.window = pygame.display.set_mode((self.windows_width, self.windows_height))
        pygame.display.set_caption("Şövalye Osman")

        self.Current_Level = TestLevel(self.windows_width, self.windows_height)

        self.Clock = pygame.time.Clock()


    def Draw(self):

        self.Current_Level.Draw(self.window)
        self.Clock.tick(60)
        pygame.display.update()


    def GameLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        self.Key = pygame.key.get_pressed()
        if self.Key[pygame.K_ESCAPE]:
            return "QUIT"

        self.Mouse = pygame.mouse.get_pressed()

        self.Current_Level.GameLoop(self.Key, self.Mouse)
        self.Draw()



Game = GameCore()

while True:
    Status = Game.GameLoop()
    if Status == "QUIT":
        break

pygame.quit()