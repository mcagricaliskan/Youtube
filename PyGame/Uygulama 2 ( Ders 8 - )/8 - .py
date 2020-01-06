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


        ####### BackGround ########
        self.BackGroundDay = pygame.image.load("Data/sprites/background-day.png").convert_alpha()
        self.BackGroundNight = pygame.image.load("Data/sprites/background-night.png").convert_alpha()
        self.BackGroundList = [self.BackGroundDay, self.BackGroundNight]
        self.BackGround = self.BackGroundList[random.randint(0,1)]
        self.BackGround_X = 0
        self.BackGround_Y = 0


        self.Ground = pygame.image.load("Data/sprites/base.png").convert_alpha()
        self.Ground_X = 0
        self.Ground_Y = 400

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

    def Draw(self):

        self.window.blit(self.BackGround, (self.BackGround_X, self.BackGround_Y))
        self.window.blit(self.Ground, (self.Ground_X,self.Ground_Y))
        self.window.blit(self.BirdList[self.BirdAnimation], (self.Bird_X, self.Bird_Y))
        self.Clock.tick(60)
        pygame.display.update()

    def GameLoop(self):


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Close"

        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Close"

        ######### Gravity ###########
        if self.Bird_Y < 380:
            self.Bird_Y += self.Gravity
            self.Gravity += self.acc


        ######### Animation #########
        if pygame.time.get_ticks() - self.BirdAnimationTime > self.BirdAnimationDelay:
            self.BirdAnimation += 1
            if self.BirdAnimation == 4:
                self.BirdAnimation = 0
            self.BirdAnimationTime = pygame.time.get_ticks()

        self.Draw()



Game = GameCore()

while True:
    GameStatus = Game.GameLoop()
    if GameStatus == "Close":
        break

pygame.quit()
