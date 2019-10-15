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
        pygame.display.set_caption("Şövalye Osman")



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
        self.FareTuslari = pygame.mouse.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Durdur"
        self.Move()
        self.Draw()


    def Move(self):
        if self.Tus[pygame.K_d]:
            self.karakter.Yon = "Sag"
            self.karakter.Durum = "Normal"
            self.karakter.Hareket = "Koşu"
            self.karakter.KaraterX+= 15
        elif self.FareTuslari[0] == 1:
            if self.karakter.Hareket == "Durus" and self.karakter.Durum == "Saldırı" and self.karakter.SaldırıSırası == 0:
                self.karakter.Hareket = "İkinciSaldırı"
                self.karakter.Animasyon = True
                self.karakter.SaldırıSırası+= 1
                print("1. saldırı")
            if self.karakter.Hareket == "Durus" and self.karakter.Durum == "Saldırı" and self.karakter.SaldırıSırası == 1:
                self.karakter.Hareket = "ÜçüncüSaldırı"
                self.karakter.Animasyon = True
                self.karakter.SaldırıSırası-=1
                print("2. saldırı")
            elif self.karakter.Hareket == "Durus" and self.karakter.Durum == "Normal":
                self.karakter.Hareket = "KılıcCek"
                self.karakter.Durum = "Saldırı"
                self.karakter.Animasyon = True
        elif self.Tus[pygame.K_a]:
            self.karakter.Yon = "Sol"
            self.karakter.Durum = "Normal"
            self.karakter.Hareket = "Koşu"
            self.karakter.KaraterX-= 15
        else:
            if self.karakter.Animasyon == False:
                self.karakter.Hareket = "Durus"


game = Game()



while True:
    if game.GenelDurum == "Game":
        Loop = game.GameLoop()
        if Loop == "Durdur":
            break






pygame.quit()