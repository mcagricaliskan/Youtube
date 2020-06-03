import pygame
import json

class Character:
    def __init__(self):
        self.C_X = 500
        self.C_Y = 500


        self.Character_Load_Files()

        self.C_HP = 100


        # self.C_Dictionary init olarak tanımlanmadığı için
        # eğer character_data.txt adında bir text yok ise
        # çalıştırdığınızda hata verebilir.
        # Daha düzgün bir ayarlama ilerleyen videolarda
        # gerçekleştirilecektir.

        self.C_Gold = self.C_Dictionary["Gold"]

        self.C_Scale = (200, 148)
        self.C_Status = "idle"
        self.C_Time = pygame.time.get_ticks()
        self.C_Direction = False
        self.C_Speed = 5

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

        ######## RUN ###########

        self.C_run_1 = pygame.image.load(self.C_Sprite_path + "adventurer-run-00.png")
        self.C_run_2 = pygame.image.load(self.C_Sprite_path + "adventurer-run-01.png")
        self.C_run_3 = pygame.image.load(self.C_Sprite_path + "adventurer-run-02.png")
        self.C_run_4 = pygame.image.load(self.C_Sprite_path + "adventurer-run-03.png")
        self.C_run_5 = pygame.image.load(self.C_Sprite_path + "adventurer-run-04.png")
        self.C_run_6 = pygame.image.load(self.C_Sprite_path + "adventurer-run-05.png")
        self.C_run_Animation = 0
        self.C_run_1 = pygame.transform.scale(self.C_run_1, self.C_Scale)
        self.C_run_2 = pygame.transform.scale(self.C_run_2, self.C_Scale)
        self.C_run_3 = pygame.transform.scale(self.C_run_3, self.C_Scale)
        self.C_run_4 = pygame.transform.scale(self.C_run_4, self.C_Scale)
        self.C_run_5 = pygame.transform.scale(self.C_run_5, self.C_Scale)
        self.C_run_6 = pygame.transform.scale(self.C_run_6, self.C_Scale)
        self.C_run_delay = 250

        self.C_run_List = [
            self.C_run_1,
            self.C_run_2,
            self.C_run_3,
            self.C_run_4,
            self.C_run_5,
            self.C_run_6
        ]
    def Character_Save_Files(self):
        self.C_Dictionary = {
            "Gold" : self.C_Gold
        }

        json.dump(self.C_Dictionary, open("Character/Character_Data.txt", "w"))

    def Character_Load_Files(self):

        self.C_Dictionary = json.load(open("Character/Character_Data.txt"))



    def Draw(self,window):

        if self.C_Status == "idle":
            window.blit(pygame.transform.flip(self.C_idle_List[self.C_idle_Animation], self.C_Direction, False),
                        (self.C_X, self.C_Y))
        elif self.C_Status == "idle_sword":
            window.blit(pygame.transform.flip(self.C_idle_sword_List[self.C_idle_sword_Animation], self.C_Direction, False),
                        (self.C_X, self.C_Y))
        elif self.C_Status == "Run":
            window.blit(pygame.transform.flip(self.C_run_List[self.C_run_Animation], self.C_Direction, False),
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

        if self.Key[pygame.K_d]:
            self.C_Status = "Run"
            self.C_Direction = False
            self.C_X += self.C_Speed

        elif self.Key[pygame.K_j]:
            self.Character_Save_Files()

        elif self.Key[pygame.K_a]:
            self.C_Status = "Run"
            self.C_Direction = True
            self.C_X -= self.C_Speed
        else:
            if self.C_Action_Mode == True:
                self.C_Status = "idle_sword"
            else:
                self.C_Status = "idle"

        if self.Mouse[0] == 1: # (1,0,0)
            if self.C_Action_Mode == False:
                self.C_Action_Mode = True
                self.C_Status = "idle_sword"

        print(self.C_Gold)

        ######## Animation #########
        if self.C_Action_Mode == False:
            if self.C_Status == "idle":
                self.C_idle_Animation = self.Animation(self.C_idle_delay,
                                                       self.C_idle_Animation, 3)

            elif self.C_Status == "Run":
                self.C_run_Animation = self.Animation(self.C_run_delay,
                                                      self.C_run_Animation, 6)

        elif self.C_Action_Mode == True:
            if self.C_Status == "idle_sword":
                self.C_idle_sword_Animation = self.Animation(self.C_idle_sword_delay,
                                                             self.C_idle_sword_Animation,
                                                             4)
            elif self.C_Status == "Run":
                self.C_run_Animation = self.Animation(self.C_run_delay,
                                                      self.C_run_Animation, 6)