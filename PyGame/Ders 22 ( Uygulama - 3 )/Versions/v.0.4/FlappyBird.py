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
        self.Score = 0





        ####### SCORE SPRİTES ###########
        self.Score0 = pygame.image.load("Data/sprites/0.png").convert_alpha()
        self.Score1 = pygame.image.load("Data/sprites/1.png").convert_alpha()
        self.Score2 = pygame.image.load("Data/sprites/2.png").convert_alpha()
        self.Score3 = pygame.image.load("Data/sprites/3.png").convert_alpha()
        self.Score4 = pygame.image.load("Data/sprites/4.png").convert_alpha()
        self.Score5 = pygame.image.load("Data/sprites/5.png").convert_alpha()
        self.Score6 = pygame.image.load("Data/sprites/6.png").convert_alpha()
        self.Score7 = pygame.image.load("Data/sprites/7.png").convert_alpha()
        self.Score8 = pygame.image.load("Data/sprites/8.png").convert_alpha()
        self.Score9 = pygame.image.load("Data/sprites/9.png").convert_alpha()
        self.ScoreList = [self.Score0, self.Score1, self.Score2, self.Score3, self.Score4, self.Score5,
                          self.Score6, self.Score7, self.Score8, self.Score9]




        ######## BİRD #########

        self.BirdDown = pygame.image.load("Data/sprites/yellowbird-downflap.png").convert_alpha()
        self.BirdMid = pygame.image.load("Data/sprites/yellowbird-midflap.png").convert_alpha()
        self.BirdUp = pygame.image.load("Data/sprites/yellowbird-upflap.png").convert_alpha()
        self.BirdList = [self.BirdMid, self.BirdDown, self.BirdUp]
        self.PipeGreen = pygame.image.load("Data/sprites/pipe-green.png").convert_alpha()
        self.PipeUpper = pygame.image.load("Data/sprites/pipe-green.png").convert_alpha()

        self.Base = pygame.image.load("Data/sprites/base.png").convert_alpha()
        self.BackGround = pygame.image.load("Data/sprites/background-day.png").convert()

    def Draw(self):
        self.clock.tick(60)
        self.Window.blit(self.BackGround, (self.BackGroundX, 0))
        self.Window.blit(self.BackGround, (self.BackGroundSecondX, 0))
        self.Window.blit(self.Base, (self.BaseX,400))
        self.Window.blit(self.Base, (self.BaseSecondX, 400))
        for Pipes in self.PipeList:
            Pipes.PipeDraw(self.Window)


        if self.Score < 10:
            self.Window.blit(self.ScoreList[self.Score],(132,20))
        elif 10 <= self.Score < 100:
            Score2 = list(str(self.Score))
            Score21 = int(Score2[0])
            Score22 = int(Score2[1])
            self.Window.blit(self.ScoreList[Score21],(119,20))
            self.Window.blit(self.ScoreList[Score22],(145,20))
        else:
            Score3 = list(str(self.Score))
            self.Window.blit(self.ScoreList[int(Score3[0])], (114, 20))
            self.Window.blit(self.ScoreList[int(Score3[1])], (132, 20))
            self.Window.blit(self.ScoreList[int(Score3[2])], (158, 20))




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





        ########## ADDİNG PİPE ############
        if pygame.time.get_ticks() - self.Time3 > self.PipeDelay:
            self.PipeList.append(self.Pipe(288,random.randint(200,350),self.PipeGreen,self.PipeUpper))
            self.Time3 = pygame.time.get_ticks()

        """
         ############ BACKGROUND MOVEMENT ############
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
                if self.BirdX + 16 == PipeMove.PipeX + 24:
                    pygame.mixer.music.play(0)
                    self.Score += 1
                    print(self.Score)

            if self.BaseX < -285:
                self.BaseX = 0
            if self.BaseSecondX < 0:
                self.BaseSecondX = 288

            self.Time2 = pygame.time.get_ticks()

        for Pipes in self.PipeList:
            ########## SCORE AND SOUND ##########

            if Pipes.PipeX < -55:
                sıra = self.PipeList.index(Pipes)
                self.PipeList.pop(sıra)

        self.Draw()


game = Game()

while True:
    Statu = game.GameLoop()
    if Statu == "Stop":
        break

pygame.quit()
