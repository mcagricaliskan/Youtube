import pygame
import random


pygame.init()


#%% Pencere


pencere_genislik = 1280
pencere_yukseklik = 1000

pencere = pygame.display.set_mode((pencere_genislik,pencere_yukseklik ))
pygame.display.set_caption("Kare")


arkaplan = pygame.image.load("Resimler/arkaplanDers2.jpg")
kareResim = pygame.image.load("Resimler/kare.jpg")
dusenKare = pygame.image.load("Resimler/kare2.jpg")

#%% Sınıflar ve Objeler

class Kare(object):
    def __init__(self,kareX,kareY,Resim,hiz):
        self.kareX = kareX
        self.kareY = kareY
        self.kareResim = Resim
        self.kareHiz = hiz
    def Cizdir(self,pencere):
        pencere.blit(self.kareResim, (self.kareX,self.kareY))
    def SagHareket(self):
        self.kareX+= self.kareHiz
    def SolHareket(self):
        self.kareX-= self.kareHiz
    def YukariHareket(self):
        self.kareY-= self.kareHiz
    def AsagiHareket(self):
        self.kareY+= self.kareHiz
        

kare = Kare(600,890,kareResim,10)
dusmanKareList = []

#%% Fonksiyonlar


def ekranCizim(pencere):
    
    pencere.blit(arkaplan, (0,0))
    kare.Cizdir(pencere)
    for kareler in dusmanKareList:
        kareler.Cizdir(pencere)
    
    
    pygame.display.update()
    

#%% Oyun döngüsü

def oyun():
    
    oyunDurumu = True
    kareSayisi = 8
    
    while oyunDurumu:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyunDurumu = False
                
        
        if len(dusmanKareList) != kareSayisi:
            dusmanKareList.append(Kare(random.randint(40,1240),0,
                                       dusenKare,random.randint(1,5)))

        
        
        for kareler in dusmanKareList:
            kareler.AsagiHareket()
 
            if kareler.kareY == 1000:
                dusmanKareList.pop(dusmanKareList.index(kareler))
                
        
        
        Tus = pygame.key.get_pressed()
        
        if Tus[pygame.K_ESCAPE]:
            oyunDurumu = False        
            
        
        #print(" x = {0} , y = {1}".format(kare.kareX,kare.kareY))
        
        if Tus[pygame.K_RIGHT] and kare.kareX < 1170:
            kare.SagHareket()
        elif Tus[pygame.K_LEFT] and kare.kareX > 10:
            kare.SolHareket()

        
        ekranCizim(pencere)
        

oyun()
pygame.quit()