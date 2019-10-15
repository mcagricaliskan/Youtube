import pygame
import time


pygame.init()



#%% Pencere
pencere_boyutu = (1920,1080)
pencere = pygame.display.set_mode(pencere_boyutu)
#pencere = pygame.display.set_mode((0,0), pygame.FULLSCREEN)


GenelDurum = "AnaMenu"
clock = pygame.time.Clock()

AnaMenuBackGround = pygame.image.load("Resimler/AnaMenuBackGround.jpg").convert_alpha()
oyunBackGround = pygame.image.load("Resimler/oyunBackGround.png").convert_alpha()
bizimGemiLoad = pygame.image.load("Resimler/bizimGemi.png").convert_alpha()
bizimLazerLoad = pygame.image.load("Resimler/bizimLazer.png").convert_alpha()



class bizimGemi(object):
    def __init__(self,bizimGemiX,bizimGemiY,bizimGemiResim):
        self.bGx = bizimGemiX 
        self.bGy = bizimGemiY
        self.bGr = bizimGemiResim
    def cizim(self,pencere):
        pencere.blit(self.bGr,(self.bGx,self.bGy))
    def SagHareket(self):
        self.bGx+= 10
    def SolaHareket(self):
        self.bGx-=10


class Lazer(object):
    def __init__(self,bizimLazerX,bizimLazerY,bizimLazerResim):
        self.bLx = bizimLazerX + 49
        self.bLy = bizimLazerY - 10
        self.hiz = 5
        self.bLr = bizimLazerResim
    def cizim(self,pencere):
        pencere.blit(self.bLr,(self.bLx,self.bLy))
    def LazerHareket(self):
        self.bLy-= self.hiz



bizimG = bizimGemi(900,900,bizimGemiLoad)
bizimLazerList = []





    
    
    


#%% Oyun Döngüsü
        
def BasilanTus(Tus):
    if Tus[pygame.K_a]:
        bizimG.SolaHareket()
    elif Tus[pygame.K_d]:
        bizimG.SagHareket()

def OyunCizim():    
    
    clock.tick(60)
    
    pencere.blit(oyunBackGround, (0,0))
    
    bizimG.cizim(pencere)
    
    for Lazerler in bizimLazerList:
        Lazerler.cizim(pencere)
    pygame.display.update()
        


def oyun():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "Durdur"
            
    
    
    Tus = pygame.key.get_pressed()
    if Tus[pygame.K_ESCAPE]:
        return "Durdur"
    

    if Tus[pygame.K_SPACE]:
        bizimLazerList.append(Lazer(bizimG.bGx,bizimG.bGy,bizimLazerLoad))    
    
    for Lazerler in bizimLazerList:
        Lazerler.LazerHareket()
    
    
    
    BasilanTus(Tus)
    OyunCizim()
        
    
    
    
    
    
    
    
    
    
    

#%% Ana Menü Döngüsü

def AnaMenuCizim():
    
    clock.tick(60)    
    pencere.blit(AnaMenuBackGround, (0,0))
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
while True:
    if GenelDurum == "AnaMenu":
        durum = AnaMenu()
        if durum == "Durdur":
            break
    elif GenelDurum == "oyun":
        durum = oyun()
        if durum == "Durdur":
            break




pygame.quit()