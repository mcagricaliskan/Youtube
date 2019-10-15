import pygame


pygame.init()



#%% Pencere
pencere_boyutu = (1920,1080)
pencere = pygame.display.set_mode(pencere_boyutu)
#pencere = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

GenelDurum = "AnaMenu"


AnaMenuBackGround = pygame.image.load("Resimler/AnaMenuBackGround.jpg")
oyunBackGround = pygame.image.load("Resimler/oyunBackGround.png")



def AnaMenuCizim():
    
    pencere.blit(AnaMenuBackGround, (0,0))
    pygame.display.update()

    
def OyunCizim():    
    
    pencere.blit(oyunBackGround, (0,0))
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