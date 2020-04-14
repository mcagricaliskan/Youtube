import pygame
import random

pygame.init()

class GameCore():
    def __init__(self):
        self.screen_width = 512
        self.screen_height = 288
        self.window = pygame.display.set_mode((self.screen_height, self.screen_width))
        pygame.display.set_caption("Flappy Bird")
        self.Clock = pygame.time.Clock()
        self.GameStatus = "Start"

        ####### BackGround ########
        self.BackGroundDay = pygame.image.load("Data/sprites/background-day.png").convert_alpha()
        self.BackGroundNight = pygame.image.load("Data/sprites/background-night.png").convert_alpha()
        self.BackGroundList = [self.BackGroundDay, self.BackGroundNight]
        self.BackGround = self.BackGroundList[random.randint(0, 1)]
        self.BackGround_X = 0
        self.BackGround_Y = 0

        self.GameStartImage = pygame.image.load("Data/sprites/message.png").convert_alpha()

        self.Ground = pygame.image.load("Data/sprites/base.png").convert_alpha()
        self.Ground_X = 0
        self.Ground_Y = 400
        self.Ground_X2 = 336
        self.Ground_Y2 = 400

        ####### Bird ########

        self.BirdUp = pygame.image.load("Data/sprites/yellowbird-upflap.png").convert_alpha()
        self.BirdMid = pygame.image.load("Data/sprites/yellowbird-midflap.png").convert_alpha()
        self.BirdDown = pygame.image.load("Data/sprites/yellowbird-downflap.png").convert_alpha()
        self.BirdList = [self.BirdMid, self.BirdUp, self.BirdMid, self.BirdDown]
        self.BirdAnimation = 0
        self.BirdAnimationDelay = 100
        self.BirdAnimationTime = pygame.time.get_ticks()
        self.Bird_X = 50
        self.Bird_Y = 50
        self.Gravity = 0.75
        self.acc = 0.075

        ##### PIPE ######
        self.pipe_list = []
        self.PIPEIMAGE = pygame.image.load("Data/sprites/pipe-green.png").convert_alpha()
        self.PipeAnimationTime = pygame.time.get_ticks()
        self.PipeAnimationDelay = 2000

    class Pipe():
        def __init__(self, pipe_X, pipe_Y, PipeImage):
            self.pipe_X = pipe_X
            self.pipe_Y = pipe_Y
            self.pipe_image = PipeImage

        def DrawPipe(self, window):
            window.blit(self.pipe_image, (self.pipe_X, self.pipe_Y))
            window.blit(pygame.transform.flip(self.pipe_image, False, True),(self.pipe_X, self.pipe_Y - 420))

        def MovePipe(self):
            self.pipe_X -= 1

    def Draw(self):

        self.window.blit(self.BackGround, (self.BackGround_X, self.BackGround_Y))

        if self.GameStatus == "Start":
            self.window.blit(self.GameStartImage, (0,0))
        if self.GameStatus == "Game":
            for pipe in self.pipe_list:
                pipe.DrawPipe(self.window)
            self.window.blit(self.BirdList[self.BirdAnimation], (self.Bird_X, self.Bird_Y))

        self.window.blit(self.Ground, (self.Ground_X, self.Ground_Y))
        self.window.blit(self.Ground, (self.Ground_X2, self.Ground_Y2))

        self.Clock.tick(60)


        pygame.display.update()

    def GameLoop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Close"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.GameStatus == "Start":
                        self.GameStatus = "Game"
                    if self.GameStatus == "Game":
                        self.Gravity = -2.8
                    if self.GameStatus == "GameOver":
                        self.GameStatus == "Start"

        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Close"


        if self.GameStatus == "Game":
            ######### Gravity ###########
            if self.Bird_Y < 380:
                self.Bird_Y += self.Gravity
                self.Gravity += self.acc

            ######## Ground Control ######

            self.Ground_X -= 1
            self.Ground_X2 -= 1

            if self.Ground_X == -336:
                self.Ground_X = 336

            if self.Ground_X2 == -336:
                self.Ground_X2 = 336

            ######### Animation #########
            if pygame.time.get_ticks() - self.BirdAnimationTime > self.BirdAnimationDelay:
                self.BirdAnimation += 1
                if self.BirdAnimation == 4:
                    self.BirdAnimation = 0
                self.BirdAnimationTime = pygame.time.get_ticks()

            ######## PIPE ###########
            if pygame.time.get_ticks() - self.PipeAnimationTime > self.PipeAnimationDelay:
                self.pipe_list.append(self.Pipe(300, random.randint(180,320), self.PIPEIMAGE))
                self.PipeAnimationTime = pygame.time.get_ticks()

            for pipe in self.pipe_list:
                pipe.MovePipe()

                if pipe.pipe_X == -52:
                    self.pipe_list.remove(pipe)

        self.Draw()


Game = GameCore()

while True:
    GameStatus = Game.GameLoop()
    if GameStatus == "Close":
        break

pygame.quit()
