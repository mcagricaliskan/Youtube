import pygame


class Character:
    def __init__(self):
        self.C_X = 500
        self.C_Y = 500

        self.C_Scale = (200, 148)
        self.C_Status = "idle"
        self.C_Time = pygame.time.get_ticks()

        self.C_Sprite_path = "Character/Character_Data/Sprite/"

        self.C_Action_Mode = False

        ###### idle #######
        self.C_idle_1 = pygame.image.load(self.C_Sprite_path + "adventurer-idle-00.png").convert_alpha()
        self.C_idle_2 = pygame.image.load(self.C_Sprite_path + "adventurer-idle-01.png").convert_alpha()
        self.C_idle_3 = pygame.image.load(self.C_Sprite_path + "adventurer-idle-02.png").convert_alpha()
        self.C_idle_Animation = 0
        self.C_idle_1 = pygame.transform.scale(self.C_idle_1, self.C_Scale)
        self.C_idle_2 = pygame.transform.scale(self.C_idle_2, self.C_Scale)
        self.C_idle_3 = pygame.transform.scale(self.C_idle_3, self.C_Scale)
        self.C_idle_delay = 250

        self.C_idle_List = [
            self.C_idle_1,
            self.C_idle_2,
            self.C_idle_3
        ]

        ######## idle with sword ########

        self.C_idle_sword_1 = pygame.image.load(self.C_Sprite_path + "adventurer-idle-2-00.png").convert_alpha()
        self.C_idle_sword_2 = pygame.image.load(self.C_Sprite_path + "adventurer-idle-2-01.png").convert_alpha()
        self.C_idle_sword_3 = pygame.image.load(self.C_Sprite_path + "adventurer-idle-2-02.png").convert_alpha()
        self.C_idle_sword_4 = pygame.image.load(self.C_Sprite_path + "adventurer-idle-2-03.png").convert_alpha()
        self.C_idle_sword_Animation = 0
        self.C_idle_sword_1 = pygame.transform.scale(self.C_idle_sword_1, self.C_Scale)
        self.C_idle_sword_2 = pygame.transform.scale(self.C_idle_sword_2, self.C_Scale)
        self.C_idle_sword_3 = pygame.transform.scale(self.C_idle_sword_3, self.C_Scale)
        self.C_idle_sword_4 = pygame.transform.scale(self.C_idle_sword_4, self.C_Scale)
        self.C_idle_sword_delay = 250

        self.C_idle_sword_List = [
            self.C_idle_sword_1,
            self.C_idle_sword_2,
            self.C_idle_sword_3,
            self.C_idle_sword_4
        ]


    def Draw(self,window):

        if self.C_Status == "idle":
            window.blit(self.C_idle_List[self.C_idle_Animation],
                        (self.C_X, self.C_Y))
        elif self.C_Status == "idle_sword":
            window.blit(self.C_idle_sword_List[self.C_idle_sword_Animation],
                        (self.C_X, self.C_Y))

    def Animation(self, Delay, animation_Number, limit_of_the_animation):
        if pygame.time.get_ticks() - self.C_Time > Delay:
            animation_Number += 1
            if animation_Number == limit_of_the_animation:
                animation_Number = 0
            self.C_Time = pygame.time.get_ticks()
        return animation_Number

    def GameLoop(self, Key, Mouse):
        self.Key = Key
        self.Mouse = Mouse

        if self.Key[pygame.K_SPACE]:
            if self.C_Action_Mode == True:
                self.C_Action_Mode = False
                self.C_Status = "idle"

        if self.Mouse[0] == 1: # (1,0,0)
            if self.C_Action_Mode == False:
                self.C_Action_Mode = True
                self.C_Status = "idle_sword"



        ######## Animation #########
        if self.C_Action_Mode == False:
            if self.C_Status == "idle":
                self.C_idle_Animation = self.Animation(self.C_idle_delay,
                                                       self.C_idle_Animation, 3)

        elif self.C_Action_Mode == True:
            if self.C_Status == "idle_sword":
                self.C_idle_sword_Animation = self.Animation(self.C_idle_sword_delay,
                                                             self.C_idle_sword_Animation,
                                                             4)