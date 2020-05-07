import pygame



class Character:
    def __init__(self):
        self.Character_X = 500
        self.Character_Y = 500



        self.Character_idle_1 = pygame.image.load("Data/Character/adventurer-idle-00.png").convert_alpha()
        self.Character_idle_2 = pygame.image.load("Data/Character/adventurer-idle-00.png").convert_alpha()
        self.Character_idle_3 = pygame.image.load("Data/Character/adventurer-idle-00.png").convert_alpha()

        self.Character_idle_1 = pygame.transform.scale(self.Character_idle_1,(200,148))
        self.Character_idle_2 = pygame.transform.scale(self.Character_idle_2, (200, 148))
        self.Character_idle_3 = pygame.transform.scale(self.Character_idle_3, (200, 148))


        self.Character_idle_List = [
            self.Character_idle_1,
            self.Character_idle_2,
            self.Character_idle_3
        ]

    def Character_Draw(self,window):

        window.blit(self.Character_idle_List[0],(self.Character_X, self.Character_Y))

    def Character_Loop(self):

        self.Character_Y += 0.7