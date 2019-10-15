import pygame


pygame.init()

class Karakter():
    def __init__(self,KarakterX,KarakterY):
        self.KaraterX = KarakterX
        self.KaraterY = KarakterY
        self.Durus1 = pygame.image.load("Data/Picture/adventurer-idle-00.png").convert_alpha()
        self.Durus2 = pygame.image.load("Data/Picture/adventurer-idle-01.png").convert_alpha()
        self.Durus3 = pygame.image.load("Data/Picture/adventurer-idle-02.png").convert_alpha()
        self.DurusList = [self.Durus1,self.Durus2,self.Durus3]
        self.i = 0
        self.Time = pygame.time.get_ticks()
        self.Delay = 250

    def Draw(self, pencere):
        pencere.blit(pygame.transform.scale(self.DurusList[self.i],(250,185)),(self.KaraterX,self.KaraterY))
        if pygame.time.get_ticks() - self.Time > self.Delay:
            self.i+=1
            if self.i == 3:
                self.i = 0
            self.Time = pygame.time.get_ticks()

