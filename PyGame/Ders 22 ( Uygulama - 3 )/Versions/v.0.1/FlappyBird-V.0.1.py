import pygame



pygame.init()

class Game():
    def __init__(self):
        self.ScreenWidth = 288
        self.ScreenHeight = 512
        self.Window = pygame.display.set_mode((self.ScreenWidth,self.ScreenHeight))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()


        ######## BİRD #########

        self.BirdDown = pygame.image.load("Data/sprites/yellowbird-downflap.png").convert_alpha()
        self.BirdMid =  pygame.image.load("Data/sprites/yellowbird-midflap.png").convert_alpha()
        self.BirdUp = pygame.image.load("Data/sprites/yellowbird-upflap.png").convert_alpha()
        self.BirdList = [self.BirdMid,self.BirdDown,self.BirdUp]


        self.BackGround = pygame.image.load("Data/sprites/background-day.png").convert_alpha()

    def Draw(self):
        self.clock.tick(60)
        self.Window.blit(self.BackGround,(0,0))
        pygame.display.update()

    def GameLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        self.Keys = pygame.key.get_pressed()

        if self.Keys[pygame.K_ESCAPE]:
            return "Stop"

        if self.Keys[pygame.K_SPACE]:
            pass


        self.Draw()


game = Game()

while True:
    Statu = game.GameLoop()
    if Statu == "Stop":
        break

pygame.quit()