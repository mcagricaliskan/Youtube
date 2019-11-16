import pygame

pygame.init()

class BizimOyun():
    def __init__(self):
        self.pencere_genislik = 1280
        self.pencere_yukseklik = 720
        self.Pencere = pygame.display.set_mode((self.pencere_genislik,self.pencere_yukseklik))
        pygame.display.set_caption("Kare Yakalama")
        self.Clock = pygame.time.Clock()

    def DrawScreen(self):

        self.Clock.tick(60)
        pygame.display.update()

    def Oyun(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Son"

        self.Tus = pygame.key.get_pressed()

        if self.Tus[pygame.K_ESCAPE]:
            return "Son"

        self.DrawScreen()


Oyun = BizimOyun()


while True:
    Durum = Oyun.Oyun()
    if Durum == "Son":
        break

pygame.quit()