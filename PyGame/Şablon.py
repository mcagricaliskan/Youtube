import pygame

pygame.init()


class BizimOyunumuz():
    def __init__(self):
        self.pencere_yuksekligi = 720
        self.pencere_genisligi = 1280
        self.Pencere = pygame.display.set_mode((self.pencere_genisligi,self.pencere_yuksekligi))
        pygame.display.set_caption("Kare Yakalama")
        self.Clock = pygame.time.Clock()

    def Cizim(self):


        self.Clock.tick(60)
        pygame.display.update()

    def Oyun(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Son"

        self.Tus = pygame.key.get_pressed()
        if self.Tus[pygame.K_ESCAPE]:
            return "Son"


        self.Cizim()



Oyun = BizimOyunumuz()

while True:
    Durum = Oyun.Oyun()
    if Durum == "Son":
        break

pygame.quit()
