import pygame
import time
import random

pygame.init()

# %% Pencere
pencere_boyutu = (1920, 1080)
pencere = pygame.display.set_mode(pencere_boyutu)
# pencere = pygame.display.set_mode((0,0), pygame.FULLSCREEN)


GenelDurum = "AnaMenu"
clock = pygame.time.Clock()

# %% Resimler ve Müzikler

# AnaMenuBackGround = pygame.image.load("Resimler/AnaMenuBackGround.jpg").convert_alpha()
oyunBackGround = pygame.image.load("Resimler/oyunBackGround.png").convert_alpha()
bizimGemiLoad = pygame.image.load("Resimler/bizimGemi.png").convert_alpha()
bizimLazerLoad = pygame.image.load("Resimler/bizimLazer.png").convert_alpha()
dusmanGemiLoad = pygame.image.load("Resimler/dusmanGemi.png").convert_alpha()
dusmanLazerLoad = pygame.image.load("Resimler/dusmanLazer.png").convert_alpha()
asteroitLoad = pygame.image.load("Resimler/asteroit.png").convert_alpha()
bizimCanLoad = pygame.image.load("Resimler/Can.png").convert_alpha()
anaMenuLoad = pygame.image.load("Resimler/AnaMenuBackGround.png").convert_alpha()
anaMenuButonLoad = pygame.image.load("Resimler/BaslaButon.png").convert_alpha()
gameOverLoad = pygame.image.load("Resimler/GameOver.png").convert_alpha()


# %% Sınıflar


class Gemi(object):
    def __init__(self, bizimGemiX, bizimGemiY, bizimGemiResim):
        self.bGx = bizimGemiX
        self.bGy = bizimGemiY
        self.bGr = bizimGemiResim

    def cizim(self, pencere):
        pencere.blit(self.bGr, (self.bGx, self.bGy))

    def SagHareket(self):
        self.bGx += 10

    def SolaHareket(self):
        self.bGx -= 10

    def Kordinatlar(self):
        return pygame.Rect(self.bGx, self.bGy, 100, 100)  # ilk önce genişlik sonra yükseklik


class Lazer(object):
    def __init__(self, bizimLazerX, bizimLazerY, bizimLazerResim, farkX, farkY, LazerHiz):
        self.bLx = bizimLazerX + farkX
        self.bLy = bizimLazerY - farkY
        self.hiz = LazerHiz
        self.bLr = bizimLazerResim

    def cizim(self, pencere):
        pencere.blit(self.bLr, (self.bLx, self.bLy))

    def LazerHareket(self):
        self.bLy -= self.hiz

    def Kordinatlar(self):
        return pygame.Rect(self.bLx, self.bLy, 3, 10)  # ilk önce genişlik sonra yükseklik


class Asteroit(object):
    def __init__(self, asteroitX, asteroitY, asteroitResim, degiskenHiz):
        self.aX = asteroitX
        self.aY = asteroitY
        self.aR = asteroitResim
        self.dH = degiskenHiz

    def cizim(self, pencere):
        pencere.blit(self.aR, (self.aX, self.aY))

    def Hareket(self):
        self.aX += self.dH

    def Kordinatlar(self):
        return pygame.Rect(self.aX, self.aY, 50, 50)


class Zaman(object):
    def __init__(self, gecikme):
        self.gecikme = gecikme
        self.sonZaman = time.time()


class Can(object):
    def __init__(self, gemiX, gemiY, canResim, hiz):
        self.cM = 3
        self.cX = gemiX
        self.cY = gemiY
        self.cR = canResim
        self.cH = hiz

    def cizim(self, pencere):
        pencere.blit(self.cR, (self.cX, self.cY))

    def Hareket(self, yon):
        if yon == "Sag":
            self.cX += self.cH
        else:
            self.cX -= self.cH


class Skor(object):
    def __init__(self):
        self.sKa = 0
        self.sKd = 0
        self.font = pygame.font.SysFont("comicsansms", 20)

    def cizim(self, pencere):
        pencere.blit(self.font.render("Düşman Katleme Sayısınız = " + str(self.sKd), True, (255, 255, 255)), (10, 950))
        pencere.blit(self.font.render("Asteroit Katleme Sayısınız = " + str(self.sKa), True, (255, 255, 255)),
                     (10, 980))


# %% Objeler ve Listeler

bizimG = Gemi(900, 900, bizimGemiLoad)
bizimCanList = [Can(bizimG.bGx, bizimG.bGy + 110, bizimCanLoad, 10),
                Can(bizimG.bGx + 35, bizimG.bGy + 110, bizimCanLoad, 10),
                Can(bizimG.bGx + 70, bizimG.bGy + 110, bizimCanLoad, 10)
                ]
bizimLazerList = []
skor = Skor()
dusmanGemileriList = []
dusmanLazerList = []
asteroitList = []
atesOrani = Zaman(0.1)
dusmanAtesOrani = Zaman(0.25)
botSayisi = 5
asteroitSayisi = 20
hareketListesi = ["Sag", "Sol"]


# %% Oyun Döngüsü


def botHareket():
    # for i in range(900):

    for Dusman in dusmanGemileriList:
        hareket = random.choice(hareketListesi)

        if hareket == "Sag":
            if Dusman.bGx < 1810:
                for i in range(3):
                    Dusman.SagHareket()
        elif hareket == "Sol":
            if Dusman.bGx > 10:
                for i in range(3):
                    Dusman.SolaHareket()


def BasilanTus(Tus):
    if Tus[pygame.K_a] and bizimG.bGx > 10:
        bizimG.SolaHareket()
        for bizimCan in bizimCanList:
            bizimCan.Hareket("Sol")
    elif Tus[pygame.K_d] and bizimG.bGx < 1810:
        bizimG.SagHareket()
        for bizimCan in bizimCanList:
            bizimCan.Hareket("Sag")


def OyunCizim():
    clock.tick(120)

    pencere.blit(oyunBackGround, (0, 0))

    bizimG.cizim(pencere)

    for Lazerler in bizimLazerList:
        Lazerler.cizim(pencere)

    for Dusmanlar in dusmanGemileriList:
        Dusmanlar.cizim(pencere)

    for Taslar in asteroitList:
        Taslar.cizim(pencere)

    for DusmanLazerler in dusmanLazerList:
        DusmanLazerler.cizim(pencere)

    for bizimCan in bizimCanList:
        bizimCan.cizim(pencere)

    skor.cizim(pencere)

    pygame.display.update()


def oyun():
    global GenelDurum, bizimCanList

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "Durdur"

    if len(dusmanGemileriList) != botSayisi:
        dusmanGemileriList.append(Gemi((random.randint(10, 1810)), 20, dusmanGemiLoad))

    if len(asteroitList) != asteroitSayisi:
        asteroitList.append(Asteroit(0, random.randint(150, 830), asteroitLoad, random.randint(5, 50)))

    if time.time() - dusmanAtesOrani.sonZaman > dusmanAtesOrani.gecikme:
        for Dusman in dusmanGemileriList:
            dusmanLazerList.append(Lazer(Dusman.bGx, Dusman.bGy, dusmanLazerLoad, 49, (-100), -5))
        dusmanAtesOrani.sonZaman = time.time()

    for DusmanLazerler in dusmanLazerList:
        DusmanLazerler.LazerHareket()
        if DusmanLazerler.bLy > 1080:
            dusmanLazerList.pop(dusmanLazerList.index(DusmanLazerler))

        if DusmanLazerler.Kordinatlar().colliderect(bizimG.Kordinatlar()):
            try:
                dusmanLazerList.pop(dusmanLazerList.index(DusmanLazerler))
                bizimCanList.pop()
                if len(bizimCanList) == 0:
                    bizimG.bGx = 900
                    bizimG.bGy = 900
                    skor.sKa = 0
                    skor.sKd = 0
                    bizimCanList = [Can(bizimG.bGx, bizimG.bGy + 110, bizimCanLoad, 10),
                                    Can(bizimG.bGx + 35, bizimG.bGy + 110, bizimCanLoad, 10),
                                    Can(bizimG.bGx + 70, bizimG.bGy + 110, bizimCanLoad, 10)
                                    ]
                    dusmanLazerList.clear()
                    bizimLazerList.clear()
                    GenelDurum = "GameOver"

            except:
                continue

    Tus = pygame.key.get_pressed()
    if Tus[pygame.K_ESCAPE]:
        return "Durdur"

    if Tus[pygame.K_SPACE]:
        if time.time() - atesOrani.sonZaman > atesOrani.gecikme:
            bizimLazerList.append(Lazer(bizimG.bGx, bizimG.bGy, bizimLazerLoad, 49, 10, 5))
            atesOrani.sonZaman = time.time()

    for Taslar in asteroitList:
        Taslar.Hareket()

        if Taslar.aX > 1920:
            asteroitList.pop(asteroitList.index(Taslar))

        for Lazerler in bizimLazerList:
            if Lazerler.Kordinatlar().colliderect(Taslar.Kordinatlar()):
                try:
                    asteroitList.pop(asteroitList.index(Taslar))
                    bizimLazerList.pop(bizimLazerList.index(Lazerler))
                    skor.sKa += 1
                except:
                    continue

        for DusmanLazer in dusmanLazerList:
            if DusmanLazer.Kordinatlar().colliderect(Taslar.Kordinatlar()):
                try:
                    asteroitList.pop(asteroitList.index(Taslar))
                    dusmanLazerList.pop(dusmanLazerList.index(DusmanLazerler))
                except:
                    continue

    for Lazerler in bizimLazerList:
        Lazerler.LazerHareket()

        if Lazerler.bLy < 0:
            bizimLazerList.pop(bizimLazerList.index(Lazerler))

        for Dusmanlar in dusmanGemileriList:
            if Lazerler.Kordinatlar().colliderect(Dusmanlar.Kordinatlar()):
                try:
                    dusmanGemileriList.pop(dusmanGemileriList.index(Dusmanlar))
                    bizimLazerList.pop(bizimLazerList.index(Lazerler))
                    skor.sKd += 1
                except:
                    continue

    botHareket()
    BasilanTus(Tus)
    OyunCizim()


# %% Ana Menü Döngüsü

def AnaMenuCizim():
    clock.tick(60)
    pencere.blit(anaMenuLoad, (0, 0))
    pencere.blit(anaMenuButonLoad, (850, 750))
    pygame.display.update()


def AnaMenu():
    global GenelDurum

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "Durdur"

    Tus = pygame.key.get_pressed()
    if Tus[pygame.K_ESCAPE]:
        return "Durdur"

    if Tus[pygame.K_p]:
        GenelDurum = "oyun"

    AnaMenuCizim()


# %% Game Over

def GameOverCizim():
    clock.tick(60)
    pencere.blit(gameOverLoad, (0, 0))
    pencere.blit(anaMenuButonLoad, (850, 750))
    pygame.display.update()


def GameOver():
    global GenelDurum

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "Durdur"

    Tus = pygame.key.get_pressed()
    if Tus[pygame.K_ESCAPE]:
        return "Durdur"

    if Tus[pygame.K_p]:
        GenelDurum = "oyun"

    GameOverCizim()


while True:
    if GenelDurum == "AnaMenu":
        durum = AnaMenu()
        if durum == "Durdur":
            break
    elif GenelDurum == "oyun":
        durum = oyun()
        if durum == "Durdur":
            break
    elif GenelDurum == "GameOver":
        durum = GameOver()
        if durum == "Durdur":
            break

pygame.quit()