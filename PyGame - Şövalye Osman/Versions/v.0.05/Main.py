import pygame
from Karakterler import Karakter

pygame.init()



class Game():
    def __init__(self):
        self.window_height = 900
        self.window_width = 1600
        self.Pencere = pygame.display.set_mode((self.window_width,self.window_height ))
        self.clock = pygame.time.Clock()
        self.GenelDurum = "Game"
        self.karakter = Karakter(600,840-185)
        self.BackGround = pygame.image.load("Data/Picture/BackGroundTree.png")
        self.BackGround = pygame.transform.scale(self.BackGround,(1600,900))
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
        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Durdur"
        self.Move()
        self.Mouse()
        self.Draw()


    def Mouse(self):
        self.FareTuslari = pygame.mouse.get_pressed()
        if self.FareTuslari[0] == 1:
            self.karakter.Hareket = "KılıcCek"
    def Move(self):
        if self.Tus[pygame.K_d]:
            self.karakter.Yon = "Sag"
            self.karakter.Hareket = "Koşu"
            self.karakter.KaraterX+= 15
        elif self.Tus[pygame.K_a]:
            self.karakter.Yon = "Sol"
            self.karakter.Hareket = "Koşu"
            self.karakter.KaraterX-= 15
        else:
            if self.karakter.Hareket != "KılıcCekiliBekle":
                self.karakter.Hareket = "None"


game = Game()



while True:
    if game.GenelDurum == "Game":
        Loop = game.GameLoop()
        if Loop == "Durdur":
            break






pygame.quit()