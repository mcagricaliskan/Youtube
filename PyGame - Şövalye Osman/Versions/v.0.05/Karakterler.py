import pygame

pygame.init()


class Karakter():
    def __init__(self, KarakterX, KarakterY):
        self.KaraterX = KarakterX
        self.KaraterY = KarakterY
        ####### KOŞU ANİMASYONU #######

        self.Kosu1 = pygame.image.load("Data/Picture/adventurer-run-00.png").convert_alpha()
        self.Kosu2 = pygame.image.load("Data/Picture/adventurer-run-01.png").convert_alpha()
        self.Kosu3 = pygame.image.load("Data/Picture/adventurer-run-02.png").convert_alpha()
        self.Kosu4 = pygame.image.load("Data/Picture/adventurer-run-03.png").convert_alpha()
        self.Kosu5 = pygame.image.load("Data/Picture/adventurer-run-04.png").convert_alpha()
        self.KosuList = [self.Kosu1, self.Kosu2, self.Kosu3, self.Kosu4, self.Kosu5]

        ####### DURUŞ ANİMASYONU ##########
        self.Durus1 = pygame.image.load("Data/Picture/adventurer-idle-00.png").convert_alpha()
        self.Durus2 = pygame.image.load("Data/Picture/adventurer-idle-01.png").convert_alpha()
        self.Durus3 = pygame.image.load("Data/Picture/adventurer-idle-02.png").convert_alpha()
        self.DurusList = [self.Durus1, self.Durus2, self.Durus3]

        ####### KILIÇ ÇEKMEK ######
        self.KılıcCek1 = pygame.image.load("Data/Picture/adventurer-swrd-drw-00.png").convert_alpha()
        self.KılıcCek2 = pygame.image.load("Data/Picture/adventurer-swrd-drw-01.png").convert_alpha()
        self.KılıcCek3 = pygame.image.load("Data/Picture/adventurer-swrd-drw-02.png").convert_alpha()
        self.KılıcCek4 = pygame.image.load("Data/Picture/adventurer-swrd-drw-03.png").convert_alpha()
        self.KılıcCekList = [self.KılıcCek1, self.KılıcCek2, self.KılıcCek3, self.KılıcCek4]


        self.D = 0
        self.K = 0
        self.KC = 0
        self.Time = pygame.time.get_ticks()
        self.Delay = 250
        self.KılıcCekDelay = 50
        self.Yon = "Sag"
        self.Hareket = "None"


    def KilicCek(self,pencere):
        ##### Kılıç Çekmek ####
        if self.Yon == "Sag":
            pencere.blit(pygame.transform.scale(self.KılıcCekList[self.KC], (250, 185)), (self.KaraterX, self.KaraterY))
        elif self.Yon == "Sol":
            CizimKilicCek = pygame.transform.flip(self.KılıcCekList[self.KC], True, False)
            pencere.blit(pygame.transform.scale(CizimKilicCek, (250, 185)),
                         (self.KaraterX, self.KaraterY))

        if pygame.time.get_ticks() - self.Time > self.KılıcCekDelay:
            self.KC += 1
            if self.KC == 4:
                self.KC = 0
            self.Time = pygame.time.get_ticks()

    def Draw(self, pencere):

        if self.Hareket == "Koşu":
            ####### KOŞU ########
            if self.Yon == "Sag":
                pencere.blit(pygame.transform.scale(self.KosuList[self.K], (250, 185)), (self.KaraterX, self.KaraterY))
            elif self.Yon == "Sol":
                CizimKosu = pygame.transform.flip(self.KosuList[self.K], True, False)
                pencere.blit(pygame.transform.scale(CizimKosu, (250, 185)), (self.KaraterX, self.KaraterY))

            if pygame.time.get_ticks() - self.Time > self.Delay:
                self.K += 1
                if self.K == 5:
                    self.K = 0
                self.Time = pygame.time.get_ticks()

        elif self.Hareket == "KılıcCek":
            self.KilicCek(pencere)


            self.Hareket = "KılıcCekiliBekle"

        elif self.Hareket == "KılıcCekiliBekle":
            if self.Yon =="Sag":
                pencere.blit(pygame.transform.scale(self.KılıcCekList[3], (250, 185)), (self.KaraterX, self.KaraterY))
            elif self.Yon == "Sol":
                KılıcCekiliBekleCizim = pygame.transform.flip(self.KılıcCekList[3], True, False)
                pencere.blit(pygame.transform.scale(KılıcCekiliBekleCizim, (250, 185)), (self.KaraterX, self.KaraterY))

        elif self.Hareket == "None":

            ########  Duruş ########
            if self.Yon == "Sag":
                pencere.blit(pygame.transform.scale(self.DurusList[self.D], (250, 185)), (self.KaraterX, self.KaraterY))
            elif self.Yon == "Sol":
                CizimDurus = pygame.transform.flip(self.DurusList[self.D], True, False)
                pencere.blit(pygame.transform.scale(CizimDurus, (250, 185)), (self.KaraterX, self.KaraterY))

            if pygame.time.get_ticks() - self.Time > self.Delay:
                self.D += 1
                if self.D == 3:
                    self.D = 0
                self.Time = pygame.time.get_ticks()
