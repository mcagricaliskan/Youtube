import pygame
import random

pygame.init()


class DusenKareler():
    def __init__(self,DKareX,DKareY,KarelerResim,Hız):
        self.DKareX = DKareX
        self.DKareY = DKareY
        self.KarelerResim = KarelerResim
        self.Hız = Hız

    def Cizim(self,Pencere):
        Pencere.blit(self.KarelerResim,(self.DKareX,self.DKareY))

    def Hareket(self):
        self.DKareY += self.Hız

    def Kordinatlar(self,Genislik,Yukseklik):
        return pygame.Rect(self.DKareX, self.DKareY, Genislik, Yukseklik)



class BizimOyunumuz():
    def __init__(self):
        self.pencere_yuksekligi = 1000
        self.pencere_genisligi = 1280
        self.Pencere = pygame.display.set_mode((self.pencere_genisligi,self.pencere_yuksekligi))
        pygame.display.set_caption("Kare Yakalama")
        self.Clock = pygame.time.Clock()

        self.ArkaPlan = pygame.image.load("Resimler/arkaplanDers2.jpg").convert_alpha()
        self.BizimKare = pygame.image.load("Resimler/kare.jpg").convert_alpha()
        self.YakalaKare = pygame.image.load("Resimler/kare2.jpg").convert_alpha()

        self.BizimKaremiz = DusenKareler(600,850, self.BizimKare,0)


        self.OyunFont = pygame.font.SysFont("Arial", 40)
        self.GameOverFont = pygame.font.SysFont("Arial", 100)

        self.KareSayısı = 10
        self.KareListesi = []

        self.Skor = 0

        self.Durum = "Start"


    def Cizim(self):

        self.Pencere.blit(self.ArkaPlan,(0,0))

        if self.Durum == "Start":
            self.Pencere.blit(self.GameOverFont.render("Kare Yakalama", True, (255, 0, 0)), (350, 300))


        elif self.Durum =="Oyun":
            self.Pencere.blit(self.OyunFont.render("Skor = " + str(self.Skor), True, (0,0,0)), (20, 50))
            for DusKare in self.KareListesi:
                DusKare.Cizim(self.Pencere)
            self.BizimKaremiz.Cizim(self.Pencere)

        elif self.Durum == "GameOver":
            self.Pencere.blit(self.GameOverFont.render("Game Over", True, (255,0,0)), (400, 300))

        self.Clock.tick(60)
        pygame.display.update()

    def Oyun(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Son"
        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Son"

        if self.Durum == "Start":
            if self.Tus[pygame.K_s]:
                self.Durum = "Oyun"

        elif self.Durum == "Oyun":


            if self.Tus[pygame.K_a]:
                self.BizimKaremiz.DKareX -= 5
            elif self.Tus[pygame.K_d]:
                self.BizimKaremiz.DKareX += 5



            if len(self.KareListesi) != self.KareSayısı:
                self.KareListesi.append(DusenKareler(random.randint(100,1200),-10,self.YakalaKare,random.randint(4,10)))

            for DusKare in self.KareListesi:
                DusKare.Hareket()

                if DusKare.DKareY > 1000:
                    DusKare.DKareY = -10
                    DusKare.DKareX = random.randint(100,1200)
                    self.Skor -= 1

                if (self.BizimKaremiz.Kordinatlar(100,100)).colliderect(DusKare.Kordinatlar(20,20)):
                    self.Skor += 1
                    DusKare.DKareY = -10
                    DusKare.DKareX = random.randint(100, 1200)
                    print(self.Skor)

            if self.Skor < -5:
                self.Durum = "GameOver"

        elif self.Durum == "GameOver":
            pass

        self.Cizim()



Oyun = BizimOyunumuz()

while True:
    Durum = Oyun.Oyun()
    if Durum == "Son":
        break

pygame.quit()
