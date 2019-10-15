import pygame


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





bizimG = bizimGemi(500,500,bizimGemiLoad)




def BasilanTus(Tus):
    if Tus[pygame.K_a]:
        bizimG.SolaHareket()
    elif Tus[pygame.K_d]:
        bizimG.SagHareket()
    


def AnaMenuCizim():
    
    clock.tick(60)
    
    pencere.blit(AnaMenuBackGround, (0,0))
    pygame.display.update()

    
def OyunCizim():    
    
    clock.tick(60)
    
    pencere.blit(oyunBackGround, (0,0))
    
    bizimG.cizim(pencere)
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



def oyun():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "Durdur"
            
    
    
    Tus = pygame.key.get_pressed()
    if Tus[pygame.K_ESCAPE]:
        return "Durdur"
            
    
    BasilanTus(Tus)
    OyunCizim()
        
        

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