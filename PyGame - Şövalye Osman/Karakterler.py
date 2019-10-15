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

        ############## SALDIRI ANİMASYONLARI ###########

        self.Saldırı11= pygame.image.load("Data/Picture/adventurer-attack1-00.png").convert_alpha()
        self.Saldırı12 = pygame.image.load("Data/Picture/adventurer-attack1-01.png").convert_alpha()
        self.Saldırı13 = pygame.image.load("Data/Picture/adventurer-attack1-02.png").convert_alpha()
        self.Saldırı14 = pygame.image.load("Data/Picture/adventurer-attack1-03.png").convert_alpha()
        self.Saldırı15 = pygame.image.load("Data/Picture/adventurer-attack1-04.png").convert_alpha()
        self.Saldırı1 = [self.Saldırı11, self.Saldırı12, self.Saldırı13, self.Saldırı14, self.Saldırı15]


        self.Saldırı21 = pygame.image.load("Data/Picture/adventurer-attack2-00.png").convert_alpha()
        self.Saldırı22 = pygame.image.load("Data/Picture/adventurer-attack2-01.png").convert_alpha()
        self.Saldırı23 = pygame.image.load("Data/Picture/adventurer-attack2-02.png").convert_alpha()
        self.Saldırı24 = pygame.image.load("Data/Picture/adventurer-attack2-03.png").convert_alpha()
        self.Saldırı25 = pygame.image.load("Data/Picture/adventurer-attack2-04.png").convert_alpha()
        self.Saldırı26 = pygame.image.load("Data/Picture/adventurer-attack2-05.png").convert_alpha()
        self.Saldırı2 = [self.Saldırı21, self.Saldırı22, self.Saldırı23, self.Saldırı24, self.Saldırı25, self.Saldırı26]


        self.Saldırı31 = pygame.image.load("Data/Picture/adventurer-attack3-00.png").convert_alpha()
        self.Saldırı32 = pygame.image.load("Data/Picture/adventurer-attack3-01.png").convert_alpha()
        self.Saldırı33 = pygame.image.load("Data/Picture/adventurer-attack3-02.png").convert_alpha()
        self.Saldırı34 = pygame.image.load("Data/Picture/adventurer-attack3-03.png").convert_alpha()
        self.Saldırı35 = pygame.image.load("Data/Picture/adventurer-attack3-04.png").convert_alpha()
        self.Saldırı36 = pygame.image.load("Data/Picture/adventurer-attack3-05.png").convert_alpha()
        self.Saldırı3 = [self.Saldırı31, self.Saldırı32, self.Saldırı33, self.Saldırı34, self.Saldırı35, self.Saldırı36]




        self.D = 0
        self.K = 0
        self.KC = 0
        self.KD = 0
        self.Sİ = 0
        self.SÜ = 0
        self.Time = pygame.time.get_ticks()
        self.Delay = 250
        self.KılıcCekDelay = 15
        self.SaldırıİkiDelay = 10
        self.Yon = "Sag"
        self.Hareket = "Durus"
        self.Durum = "Normal"
        self.Animasyon = False
        self.SaldırıSırası = 0



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
                self.İlkSaldırı = self.KılıcCekList + self.Saldırı1
                ############ KILIÇ ÇEKMEK ##########
                if self.Yon == "Sag":
                    pencere.blit(pygame.transform.scale(self.İlkSaldırı[self.KC], (250, 185)), (self.KaraterX, self.KaraterY))
                elif self.Yon == "Sol":
                    CizimKılıcCek = pygame.transform.flip(self.İlkSaldırı[self.KC], True, False)
                    pencere.blit(pygame.transform.scale(CizimKılıcCek, (250, 185)),
                                 (self.KaraterX, self.KaraterY))

                if pygame.time.get_ticks() - self.Time > self.KılıcCekDelay:
                    self.KC += 1
                    if self.KC == 4:
                        self.KılıcCekDelay = 10
                    if self.KC == 9:
                        self.KC = 0
                        self.KılıcCekDelay = 30
                        self.Animasyon = False
                    self.Time = pygame.time.get_ticks()

            elif self.Hareket == "İkinciSaldırı":
                ############## İKİNCİ SALDIRI #############
                if self.Yon == "Sag":
                    pencere.blit(pygame.transform.scale(self.Saldırı2[self.Sİ], (250, 185)),
                                 (self.KaraterX, self.KaraterY))
                elif self.Yon == "Sol":
                    CizimKılıcDurus = pygame.transform.flip(self.Saldırı2[self.Sİ], True, False)
                    pencere.blit(pygame.transform.scale(CizimKılıcDurus, (250, 185)),
                                 (self.KaraterX, self.KaraterY))

                if pygame.time.get_ticks() - self.Time > self.SaldırıİkiDelay:
                    self.Sİ += 1
                    if self.Sİ == 6:
                        self.Sİ = 0
                        self.Animasyon = False
                    self.Time = pygame.time.get_ticks()

            elif self.Hareket == "ÜçüncüSaldırı":
                ############## ÜÇÜNCÜ SALDIRI #############
                if self.Yon == "Sag":
                    pencere.blit(pygame.transform.scale(self.Saldırı3[self.SÜ], (250, 185)),
                                 (self.KaraterX, self.KaraterY))
                elif self.Yon == "Sol":
                    CizimKılıcDurus = pygame.transform.flip(self.Saldırı3[self.SÜ], True, False)
                    pencere.blit(pygame.transform.scale(CizimKılıcDurus, (250, 185)),
                                 (self.KaraterX, self.KaraterY))

                if pygame.time.get_ticks() - self.Time > self.SaldırıİkiDelay:
                    self.SÜ += 1
                    if self.SÜ == 6:
                        self.SÜ = 0
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