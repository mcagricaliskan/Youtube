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


        ###### KILIÇ ÇEK VE BEKLE ########
        self.KılıcDurus1 = pygame.image.load("Data/Picture/adventurer-idle-2-00.png").convert_alpha()
        self.KılıcDurus2 = pygame.image.load("Data/Picture/adventurer-idle-2-01.png").convert_alpha()
        self.KılıcDurus3 = pygame.image.load("Data/Picture/adventurer-idle-2-02.png").convert_alpha()
        self.KılıcDurus4 = pygame.image.load("Data/Picture/adventurer-idle-2-03.png").convert_alpha()
        self.KılıcDurusList = [self.KılıcDurus1, self.KılıcDurus2, self.KılıcDurus3, self.KılıcDurus4]



        self.D = 0
        self.K = 0
        self.KC = 0
        self.KD = 0
        self.Time = pygame.time.get_ticks()
        self.Delay = 250
        self.KılıcCekDelay = 150
        self.Yon = "Sag"
        self.Hareket = "Durus"
        self.Durum = "Normal"
        self.Animasyon = False


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
        ################ NORMAL #######################
        if self.Durum == "Normal":
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

            elif self.Hareket == "Durus":

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

        ############### SALDIRI ##############

        elif self.Durum == "Saldırı":

            if self.Hareket == "KılıcCek":
                ############ KILIÇ ÇEKMEK ##########
                if self.Yon == "Sag":
                    pencere.blit(pygame.transform.scale(self.KılıcCekList[self.KC], (250, 185)), (self.KaraterX, self.KaraterY))
                elif self.Yon == "Sol":
                    CizimKılıcCek = pygame.transform.flip(self.KılıcCekList[self.KC], True, False)
                    pencere.blit(pygame.transform.scale(CizimKılıcCek, (250, 185)),
                                 (self.KaraterX, self.KaraterY))

                if pygame.time.get_ticks() - self.Time > self.KılıcCekDelay:
                    self.KC += 1
                    if self.KC == 4:
                        self.KC = 0
                        self.Animasyon = False
                    self.Time = pygame.time.get_ticks()

            elif self.Hareket == "Durus":
                if self.Yon == "Sag":
                    pencere.blit(pygame.transform.scale(self.KılıcDurusList[self.KD], (250, 185)),
                                 (self.KaraterX, self.KaraterY))
                elif self.Yon == "Sol":
                    CizimKılıcDurus = pygame.transform.flip(self.KılıcDurusList[self.KD], True, False)
                    pencere.blit(pygame.transform.scale(CizimKılıcDurus, (250, 185)),
                                 (self.KaraterX, self.KaraterY))

                if pygame.time.get_ticks() - self.Time > self.Delay:
                    self.KD += 1
                    if self.KD == 4:
                        self.KD = 0
                    self.Time = pygame.time.get_ticks()