import pygame



pygame.init()


#%% Pencere


pencere_genislik = 1280
pencere_yukseklik = 720

pencere = pygame.display.set_mode((pencere_genislik,pencere_yukseklik ))
pygame.display.set_caption("Kare")


arkaplan = pygame.image.load("Resimler/arkaplan.jpg")
kareResim = pygame.image.load("Resimler/kare.jpg")



class Kare(object):
    def __init__(self,kareX,kareY,Resim):
        self.kareX = kareX
        self.kareY = kareY
        self.kareResim = Resim
    def Cizdir(self,pencere):
        pencere.blit(self.kareResim, (self.kareX,self.kareY))
    def SagHareket(self):
        self.kareX+= 5
    def SolHareket(self):
        self.kareX-= 5
    def YukariHareket(self):
        self.kareY-= 5
    def AsagiHareket(self):
        self.kareY+= 5
        

kare = Kare(500,500,kareResim)


def ekranCizim(pencere):
    
    pencere.blit(arkaplan, (0,0))
    kare.Cizdir(pencere)
    pygame.display.update()


def oyun():
    
    oyunDurumu = True
    
    while oyunDurumu:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyunDurumu = False
                
        
        
        
        Tus = pygame.key.get_pressed()
        
        if Tus[pygame.K_ESCAPE]:
            oyunDurumu = False
            
            
        if Tus[pygame.K_RIGHT]:
            kare.SagHareket()
        elif Tus[pygame.K_LEFT]:
            kare.SolHareket()
        elif Tus[pygame.K_UP]:
            kare.YukariHareket()
        elif Tus[pygame.K_DOWN]:
            kare.AsagiHareket()
        
        ekranCizim(pencere)
        
        
        

oyun()
pygame.quit()