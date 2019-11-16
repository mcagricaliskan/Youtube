import pygame

pygame.init()




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

        self.BizimKareX = 500
        self.BizimKareY = 500

        self.DusenKareX = 200
        self.DusenKareY = 200

    def Cizim(self):

        self.Pencere.blit(self.ArkaPlan,(0,0))
        self.Pencere.blit(self.BizimKare, (self.BizimKareX, self.BizimKareY))
        self.Pencere.blit(self.YakalaKare, (self.DusenKareX, self.DusenKareY))


        self.Clock.tick(60)
        pygame.display.update()

    def Oyun(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Son"

        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Son"

        self.DusenKareY += 5
        if self.DusenKareY > 1000:
            self.DusenKareY = 0

        if self.Tus[pygame.K_a]:
            self.BizimKareX -= 5
        elif self.Tus[pygame.K_d]:
            self.BizimKareX += 5


        self.Cizim()



Oyun = BizimOyunumuz()

while True:
    Durum = Oyun.Oyun()
    if Durum == "Son":
        break

pygame.quit()
