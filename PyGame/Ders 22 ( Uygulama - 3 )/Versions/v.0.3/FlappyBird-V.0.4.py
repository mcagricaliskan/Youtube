import pygame
import random

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
        self.Time3 =pygame.time.get_ticks()
        self.Delay = 100
        self.DelayBase = 200
        self.BaseX = 0
        self.BaseSecondX = 288
        self.PipeList = []
        self.PipeDelay = 2500
        self.BirdX = 50
        self.BirdY = 200
        self.Point = pygame.mixer.music.load("Data/audio/point.wav")
        self.Gravity = 0.75
        self.acc = 0.075

        ######## BİRD #########

        self.BirdDown = pygame.image.load("Data/sprites/yellowbird-downflap.png").convert_alpha()
        self.BirdMid = pygame.image.load("Data/sprites/yellowbird-midflap.png").convert_alpha()
        self.BirdUp = pygame.image.load("Data/sprites/yellowbird-upflap.png").convert_alpha()
        self.BirdList = [self.BirdMid, self.BirdDown, self.BirdUp]
        self.PipeGreen = pygame.image.load("Data/sprites/pipe-green.png").convert_alpha()
        self.PipeUpper = pygame.image.load("Data/sprites/pipe-green.png").convert_alpha()

        self.Base = pygame.image.load("Data/sprites/base.png").convert()
        self.BackGround = pygame.image.load("Data/sprites/background-day.png").convert()

    def Draw(self):
        self.clock.tick(60)
        self.Window.blit(self.BackGround, (self.BackGroundX, 0))
        self.Window.blit(self.BackGround, (self.BackGroundSecondX, 0))
        self.Window.blit(self.Base, (self.BaseX,400))
        self.Window.blit(self.Base, (self.BaseSecondX, 400))
        for Pipes in self.PipeList:
            Pipes.PipeDraw(self.Window)

        self.Window.blit(self.BirdMid, (self.BirdX,self.BirdY))

        pygame.display.update()

    class Pipe():
        def __init__(self,PipeX,PipeY,PipeGreen,PipeUpper):
            self.PipeX = PipeX
            self.PipeY = PipeY
            self.PipeGreen = PipeGreen
            self.PipeUpper = PipeUpper

        def PipeDraw(self,Window):
            Window.blit(self.PipeGreen,(self.PipeX,self.PipeY))
            Window.blit(pygame.transform.flip(self.PipeUpper, False,True),(self.PipeX,self.PipeY-420))


    def GameLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Stop"
        self.Keys = pygame.key.get_pressed()
        if self.Keys[pygame.K_ESCAPE]:
            return "Stop"

        ########## GRAVİTY ##########
        if self.BirdY < 380:
            self.BirdY+= self.Gravity
            self.Gravity+= self.acc


        if self.Keys[pygame.K_SPACE] and self.BirdY > 0:
            self.BirdY-=2.75
            self.Gravity = 0.75


        for Pipes in self.PipeList:

            if Pipes.PipeX < -55:
                sıra = self.PipeList.index(Pipes)
                self.PipeList.pop(sıra)

            print(len(self.PipeList))

            ########## SCORE AND SOUND ##########
            if self.BirdX+16 == Pipes.PipeX+24:
                pygame.mixer.music.play(0)
        ########## ADDİNG PİPE
        if pygame.time.get_ticks() - self.Time3 > self.PipeDelay:
            self.PipeList.append(self.Pipe(288,random.randint(200,350),self.PipeGreen,self.PipeUpper))
            self.Time3 = pygame.time.get_ticks()

        """
        if pygame.time.get_ticks() - self.Time > self.Delay:
            self.BackGroundX -= 0
            self.BackGroundSecondX -= 0
            

            if self.BackGroundX <= -287:
                self.BackGroundX = 0
            if self.BackGroundSecondX <= 1:
                self.BackGroundSecondX = 288

            self.Time = pygame.time.get_ticks()
        """
        if pygame.time.get_ticks() - self.Time2 > self.Delay:
            self.BaseX -= 6
            self.BaseSecondX -= 6
            for PipeMove in self.PipeList:
                PipeMove.PipeX -= 6
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
