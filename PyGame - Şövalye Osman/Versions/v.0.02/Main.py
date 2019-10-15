import pygame
from Karakterler import Karakter

pygame.init()



class Game():
    def __init__(self):
        self.window_height = 720
        self.window_width = 1280
        self.Pencere = pygame.display.set_mode((self.window_width,self.window_height ))
        self.clock = pygame.time.Clock()
        self.GenelDurum = "Game"
        self.karakter = Karakter(500,300)
        self.BackGround = pygame.image.load("Data/Picture/BackGround.png")
        pygame.display.set_caption("Şovalye Osman")



    def Draw(self):
        self.clock.tick(60)
        self.Pencere.blit(self.BackGround,(0,0))
        self.karakter.Draw(self.Pencere)
        pygame.display.update()


    def GameLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Durdur"

        Tus = pygame.key.get_pressed()
        if Tus[pygame.K_ESCAPE]:
            return "Durdur"

        self.Draw()



game = Game()



while True:
    if game.GenelDurum == "Game":
        Loop = game.GameLoop()
        if Loop == "Durdur":
            break






pygame.quit()