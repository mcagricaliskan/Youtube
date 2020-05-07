import pygame
from Character import Character

pygame.init()

class GameCore:
    def __init__(self):
        self.windows_width = 1600
        self.windows_height = 900
        self.window = pygame.display.set_mode((self.windows_width, self.windows_height))
        pygame.display.set_caption("Şövalye Osman")


        self.Test_BackGround = pygame.image.load("Data/Character/BackGroundTree.png").convert()
        self.Test_BackGround = pygame.transform.scale(self.Test_BackGround,(self.windows_width,self.windows_height))
        self.Character = Character()

        self.Clock = pygame.time.Clock()


    def Draw(self):

        self.window.blit(self.Test_BackGround,(0,0))
        self.Character.Character_Draw(self.window)

        self.Clock.tick(60)
        pygame.display.update()


    def GameLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        self.Key = pygame.key.get_pressed()
        if self.Key[pygame.K_ESCAPE]:
            return "QUIT"


        self.Character.Character_Loop()
        self.Draw()



Game = GameCore()

while True:
    Status = Game.GameLoop()
    if Status == "QUIT":
        break

pygame.quit()