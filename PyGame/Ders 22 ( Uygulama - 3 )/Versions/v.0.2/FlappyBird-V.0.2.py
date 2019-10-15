import pygame

pygame.init()


class Game():
    def __init__(self):
        self.ScreenWidth = 288
        self.ScreenHeight = 512
        self.Window = pygame.display.set_mode((self.ScreenWidth, self.ScreenHeight))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.BackGroundX = 0
        self.BackGroundSecondX = 288
        self.Time = pygame.time.get_ticks()
        self.Time2 = pygame.time.get_ticks()
        self.Delay = 100
        self.DelayBase = 200
        self.BaseX = 0
        self.BaseSecondX = 288

        ######## BİRD #########

        self.BirdDown = pygame.image.load("Data/sprites/yellowbird-downflap.png").convert_alpha()
        self.BirdMid = pygame.image.load("Data/sprites/yellowbird-midflap.png").convert_alpha()
        self.BirdUp = pygame.image.load("Data/sprites/yellowbird-upflap.png").convert_alpha()
        self.BirdList = [self.BirdMid, self.BirdDown, self.BirdUp]


        self.Base = pygame.image.load("Data/sprites/base.png").convert()
        self.BackGround = pygame.image.load("Data/sprites/background-day.png").convert()

    def Draw(self):
        self.clock.tick(60)
        self.Window.blit(self.BackGround, (self.BackGroundX, 0))
        self.Window.blit(self.BackGround, (self.BackGroundSecondX, 0))
        self.Window.blit(self.Base, (self.BaseX,400))
        self.Window.blit(self.Base, (self.BaseSecondX, 400))
        self.Window.blit(self.BirdMid, (30,200))

        pygame.display.update()

    def GameLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Stop"

        self.Keys = pygame.key.get_pressed()

        if self.Keys[pygame.K_ESCAPE]:
            return "Stop"

        if self.Keys[pygame.K_SPACE]:
            pass

        if pygame.time.get_ticks() - self.Time > self.Delay:
            self.BackGroundX -= 2
            self.BackGroundSecondX -= 2
            if self.BackGroundX < -285:
                self.BackGroundX = 0
            if self.BackGroundSecondX < 0:
                self.BackGroundSecondX = 288

            self.Time = pygame.time.get_ticks()

        if pygame.time.get_ticks() - self.Time2 > self.Delay:
            self.BaseX -= 2
            self.BaseSecondX -= 2
            if self.BaseX < -285:
                self.BaseX = 0
            if self.BaseSecondX < 0:
                self.BaseSecondX = 288

            self.Time2 = pygame.time.get_ticks()

        self.Draw()


game = Game()

while True:
    Statu = game.GameLoop()
    if Statu == "Stop":
        break

pygame.quit()
