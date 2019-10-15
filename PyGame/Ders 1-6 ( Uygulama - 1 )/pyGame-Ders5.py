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


def BasilanTus(Tus):          
    if Tus[pygame.K_RIGHT] and kare.kareX < 1170:
        kare.SagHareket()
    elif Tus[pygame.K_LEFT] and kare.kareX > 10:
        kare.SolHareket()




def silinecekDusman(silinecek):
    sayac = 0
    donguDurumu = True
    while donguDurumu:
        silinecek-= 40
        sayac+= 1
        if silinecek < 0:
            donguDurumu = False
    
    return sayac




def SkorYazisi(skor):
    text = str(skor)
    font = pygame.font.SysFont("comicsansms", 60 )
    renk = (0,0,0)
    text = font.render(text, True, renk)
    return text


def ekranCizim(pencere,skor):
    
    pencere.blit(arkaplan, (0,0))
    kare.Cizdir(pencere)
    for kareler in dusmanKareList:
        kareler.Cizdir(pencere)
    pencere.blit(SkorYazisi(skor), (10,10))
    
    pygame.display.update()
    

#%% Oyun döngüsü

def oyun():
    
    oyunDurumu = True
    kareSayisi = 10
    skor = 0
    
    while oyunDurumu:
        
        
        
        KareKordinatList = []
        dusmanKareKordinatList = []
        KareKordinatList.clear()
        dusmanKareKordinatList.clear()
        
        
        
        
        for l in range(0,100,5):
            for m in range(0,100,10):
                KareKordinatList.append([kare.kareX+l,kare.kareY+m])
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyunDurumu = False
                
        
        if len(dusmanKareList) != kareSayisi:
            dusmanKareList.append(Kare(random.randint(40,1240),0,
                                       dusenKare,random.randint(5,10)))

        
        
        for kareler in dusmanKareList:
            kareler.AsagiHareket()
            
            for i in range(0,20,2):
                for k in range(0,20,5):
                    dusmanKareKordinatList.append([kareler.kareX+i,kareler.kareY+k])
                    
            if kareler.kareY > 1000:
                dusmanKareList.pop(dusmanKareList.index(kareler))
                
        
        silinecek = 0
        
        for bizim in KareKordinatList:
            for dusman in dusmanKareKordinatList:
                if bizim == dusman:
                    silinecek = dusmanKareKordinatList.index(dusman)
                    
        if silinecek != 0:
            silinen = silinecekDusman(silinecek)
            dusmanKareList.pop((silinen-1))
            skor+= 1
        
        
        Tus = pygame.key.get_pressed()
        if Tus[pygame.K_ESCAPE]:
            oyunDurumu = False   
        BasilanTus(Tus)
        
        

        
        ekranCizim(pencere,skor)
        

oyun()
pygame.quit()