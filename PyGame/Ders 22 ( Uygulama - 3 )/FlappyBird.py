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
        self.Time3 = pygame.time.get_ticks()
        self.Time4 = pygame.time.get_ticks()
        self.Time5 = pygame.time.get_ticks()
        self.Delay = 50
        self.DelayBase = 200
        self.BirdDelay = 400
        self.BaseX = 0
        self.BaseSecondX = 336
        self.PipeList = []
        self.PipeDelay = 1250
        self.BirdX = 50
        self.BirdY = 200
        self.Gravity = 0.75
        self.acc = 0.075
        self.Score = 0
        self.GameStatus ="GameStart"
        self.JumpVel = 35.75






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
        self.BirdList = [self.BirdMid, self.BirdUp, self.BirdMid, self.BirdDown]
        self.BP = 0
        self.PipeGreen = pygame.image.load("Data/sprites/pipe-green.png").convert_alpha()
        self.PipeUpper = pygame.image.load("Data/sprites/pipe-green.png").convert_alpha()

        self.Base = pygame.image.load("Data/sprites/base.png").convert_alpha()
        self.BackGround = pygame.image.load("Data/sprites/background-day.png").convert()
        self.GameOverImage = pygame.image.load("Data/sprites/gameover.png").convert_alpha()
        self.GameStartImage = pygame.image.load("Data/sprites/message.png").convert_alpha()


    def get_mask(self,Image1,Image1x,Image1y,Image2,Image2x,Image2y):
        Image1_mask = pygame.mask.from_surface(Image1)
        Image2_mask = pygame.mask.from_surface(Image2)
        offset = (round(Image2x - Image1x), round(Image2y - Image1y))
        result = Image1_mask.overlap(Image2_mask, offset)
        return result


    def Draw(self):
        self.clock.tick(60)
        self.Window.blit(self.BackGround, (self.BackGroundX, 0))
        self.Window.blit(self.BackGround, (self.BackGroundSecondX, 0))
        self.Window.blit(self.Base, (self.BaseX,400))
        self.Window.blit(self.Base, (self.BaseSecondX, 400))
        for Pipes in self.PipeList:
            Pipes.PipeDraw(self.Window)

        if self.GameStatus == "GameOver" or self.GameStatus == "Game":
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

            self.Window.blit(self.BirdPicture, (self.BirdX, self.BirdY))

        if self.GameStatus == "GameStart":
            self.Window.blit(self.GameStartImage, (50,100))

        if self.GameStatus == "GameOver":
            self.Window.blit(self.GameOverImage,(50,200))

        pygame.display.update()

    class Pipe():
        def __init__(self,PipeX,PipeY,PipeGreen,PipeUpper):
            self.PipeX = PipeX
            self.PipeY = PipeY
            self.PipeGreen = PipeGreen
            self.PipeUpper = PipeUpper
            self.PiperUpperY = self.PipeY-420

        def PipeDraw(self,Window):
            Window.blit(self.PipeGreen,(self.PipeX,self.PipeY))
            Window.blit(pygame.transform.flip(self.PipeUpper, False,True),(self.PipeX,self.PipeY-420))


    def GameLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Stop"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.BirdY > 0:
                    if self.GameStatus == "GameStart":
                        self.BirdY = 200
                        self.Gravity = 0.75
                        self.GameStatus = "Game"
                    if self.GameStatus == "Game":
                        self.BirdY -= self.JumpVel
                        self.Gravity = 0.75
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound("Data/audio/wing.ogg"))
                    if self.GameStatus == "GameOver":
                        self.PipeList.clear()
                        self.BirdY = 200
                        self.Gravity = 0.75
                        self.Score = 0
                        self.GameStatus = "GameStart"

        ########## GRAVİTY ##########
        if self.BirdY < 380:
            self.BirdY += self.Gravity
            self.Gravity += self.acc

        self.Keys = pygame.key.get_pressed()
        if self.Keys[pygame.K_ESCAPE]:
            return "Stop"

        if self.GameStatus == "Game":
            self.BirdPicture = self.BirdList[self.BP]
            if pygame.time.get_ticks() - self.Time5 > self.Delay:
                self.BP+=1
                if self.BP == 4:
                    self.BP = 0
                self.Time5 = pygame.time.get_ticks()

            if self.BirdY > 375:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("Data/audio/hit.ogg"))
                self.GameStatus = "GameOver"
            ########## ADDİNG PİPE ############
            if pygame.time.get_ticks() - self.Time3 > self.PipeDelay:
                self.PipeList.append(self.Pipe(288,random.randint(200,350),self.PipeGreen,self.PipeUpper))
                self.Time3 = pygame.time.get_ticks()

            if pygame.time.get_ticks() - self.Time2 > self.Delay:
                self.BaseX -= 6
                self.BaseSecondX -= 6
                if self.BaseX < -335:
                    self.BaseX = 0
                if self.BaseSecondX < 1:
                    self.BaseSecondX = 336

                self.Time2 = pygame.time.get_ticks()

            if pygame.time.get_ticks() - self.Time4 > self.Delay:
                for PipeMove in self.PipeList:
                    PipeMove.PipeX -= 6
                    if self.BirdX + 16 == PipeMove.PipeX + 24:
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound("Data/audio/point.ogg"))
                        self.Score += 1
                        print(self.Score)
                self.Time4 = pygame.time.get_ticks()

            for Pipes in self.PipeList:
                if Pipes.PipeX < -55:
                    sıra = self.PipeList.index(Pipes)
                    self.PipeList.pop(sıra)

                self.Result = self.get_mask(self.BirdPicture,self.BirdX,self.BirdY,Pipes.PipeGreen,Pipes.PipeX,Pipes.PipeY)
                self.Result2 = self.get_mask(self.BirdPicture, self.BirdX, self.BirdY, Pipes.PipeUpper, Pipes.PipeX, Pipes.PiperUpperY)
                if self.Result or self.Result2:
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound("Data/audio/hit.ogg"))
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Data/audio/die.ogg"))
                    self.GameStatus = "GameOver"




        self.Draw()


game = Game()

while True:
    Statu = game.GameLoop()
    if Statu == "Stop":
        break

pygame.quit()
