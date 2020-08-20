import pygame
import json


class Character:
    def __init__(self):
        self.x = 200
        self.y = 700

        self.Character_Load_Files()

        self.C_HP = 100

        # self.C_Dictionary init olarak tanımlanmadığı için
        # eğer character_data.txt adında bir text yok ise
        # çalıştırdığınızda hata verebilir.
        # Daha düzgün bir ayarlama ilerleyen videolarda
        # gerçekleştirilecektir.

        self.gold = self.save["Gold"]

        self.scale = (200, 148)
        self.status = "idle"
        self.time = pygame.time.get_ticks()
        self.direction = False
        self.speed = 5

        self.sprite_path = "Character/Character_Data/Sprite/"

        self.action_mode = False
        self.animation_mode = False

        ###### idle #######
        self.idle_1 = pygame.image.load(self.sprite_path + "adventurer-idle-00.png").convert_alpha()
        self.idle_2 = pygame.image.load(self.sprite_path + "adventurer-idle-01.png").convert_alpha()
        self.idle_3 = pygame.image.load(self.sprite_path + "adventurer-idle-02.png").convert_alpha()
        self.idle_animation = 0
        self.idle_1 = pygame.transform.scale(self.idle_1, self.scale)
        self.idle_2 = pygame.transform.scale(self.idle_2, self.scale)
        self.idle_3 = pygame.transform.scale(self.idle_3, self.scale)
        self.idle_delay = 250

        self.idle_list = [
            self.idle_1,
            self.idle_2,
            self.idle_3
        ]

        ######## idle with sword ########

        self.C_idle_sword_1 = pygame.image.load(self.sprite_path + "adventurer-idle-2-00.png").convert_alpha()
        self.C_idle_sword_2 = pygame.image.load(self.sprite_path + "adventurer-idle-2-01.png").convert_alpha()
        self.C_idle_sword_3 = pygame.image.load(self.sprite_path + "adventurer-idle-2-02.png").convert_alpha()
        self.C_idle_sword_4 = pygame.image.load(self.sprite_path + "adventurer-idle-2-03.png").convert_alpha()
        self.C_idle_sword_Animation = 0
        self.C_idle_sword_1 = pygame.transform.scale(self.C_idle_sword_1, self.scale)
        self.C_idle_sword_2 = pygame.transform.scale(self.C_idle_sword_2, self.scale)
        self.C_idle_sword_3 = pygame.transform.scale(self.C_idle_sword_3, self.scale)
        self.C_idle_sword_4 = pygame.transform.scale(self.C_idle_sword_4, self.scale)
        self.C_idle_sword_delay = 250

        self.C_idle_sword_List = [
            self.C_idle_sword_1,
            self.C_idle_sword_2,
            self.C_idle_sword_3,
            self.C_idle_sword_4
        ]

        ######## RUN ###########

        self.C_run_1 = pygame.image.load(self.sprite_path + "adventurer-run-00.png")
        self.C_run_2 = pygame.image.load(self.sprite_path + "adventurer-run-01.png")
        self.C_run_3 = pygame.image.load(self.sprite_path + "adventurer-run-02.png")
        self.C_run_4 = pygame.image.load(self.sprite_path + "adventurer-run-03.png")
        self.C_run_5 = pygame.image.load(self.sprite_path + "adventurer-run-04.png")
        self.C_run_6 = pygame.image.load(self.sprite_path + "adventurer-run-05.png")
        self.C_run_Animation = 0
        self.C_run_1 = pygame.transform.scale(self.C_run_1, self.scale)
        self.C_run_2 = pygame.transform.scale(self.C_run_2, self.scale)
        self.C_run_3 = pygame.transform.scale(self.C_run_3, self.scale)
        self.C_run_4 = pygame.transform.scale(self.C_run_4, self.scale)
        self.C_run_5 = pygame.transform.scale(self.C_run_5, self.scale)
        self.C_run_6 = pygame.transform.scale(self.C_run_6, self.scale)
        self.C_run_delay = 250

        self.C_run_List = [
            self.C_run_1,
            self.C_run_2,
            self.C_run_3,
            self.C_run_4,
            self.C_run_5,
            self.C_run_6
        ]

        self.C_draw_sword_1 = pygame.image.load(self.sprite_path + "adventurer-swrd-drw-00.png").convert_alpha()
        self.C_draw_sword_2 = pygame.image.load(self.sprite_path + "adventurer-swrd-drw-01.png").convert_alpha()
        self.C_draw_sword_3 = pygame.image.load(self.sprite_path + "adventurer-swrd-drw-02.png").convert_alpha()
        self.C_draw_sword_4 = pygame.image.load(self.sprite_path + "adventurer-swrd-drw-03.png").convert_alpha()
        self.C_draw_sword_Animation = 0
        self.C_draw_sword_1 = pygame.transform.scale(self.C_draw_sword_1, self.scale)
        self.C_draw_sword_2 = pygame.transform.scale(self.C_draw_sword_2, self.scale)
        self.C_draw_sword_3 = pygame.transform.scale(self.C_draw_sword_3, self.scale)
        self.C_draw_sword_4 = pygame.transform.scale(self.C_draw_sword_4, self.scale)
        self.C_draw_sword_delay = 50

        self.C_draw_sword_List = [
            self.C_draw_sword_1,
            self.C_draw_sword_2,
            self.C_draw_sword_3,
            self.C_draw_sword_4,
        ]

        self.C_draw_sword_back_List = [
            self.C_draw_sword_4,
            self.C_draw_sword_3,
            self.C_draw_sword_2,
            self.C_draw_sword_1,
        ]

        self.C_attack_one_1 = pygame.image.load(self.sprite_path + "adventurer-attack1-00.png").convert_alpha()
        self.C_attack_one_2 = pygame.image.load(self.sprite_path + "adventurer-attack1-01.png").convert_alpha()
        self.C_attack_one_3 = pygame.image.load(self.sprite_path + "adventurer-attack1-02.png").convert_alpha()
        self.C_attack_one_4 = pygame.image.load(self.sprite_path + "adventurer-attack1-03.png").convert_alpha()
        self.C_attack_one_5 = pygame.image.load(self.sprite_path + "adventurer-attack1-04.png").convert_alpha()
        self.C_attack_one_Animation = 0
        self.C_attack_one_1 = pygame.transform.scale(self.C_attack_one_1, self.scale)
        self.C_attack_one_2 = pygame.transform.scale(self.C_attack_one_2, self.scale)
        self.C_attack_one_3 = pygame.transform.scale(self.C_attack_one_3, self.scale)
        self.C_attack_one_4 = pygame.transform.scale(self.C_attack_one_4, self.scale)
        self.C_attack_one_5 = pygame.transform.scale(self.C_attack_one_5, self.scale)
        self.C_attack_one_delay = 50

        self.C_attack_one_List = [
            self.C_attack_one_1,
            self.C_attack_one_2,
            self.C_attack_one_3,
            self.C_attack_one_4,
            self.C_attack_one_5
        ]

    def save_files(self):
        self.save = {
            "Gold" : self.gold
        }

        json.dump(self.save, open("Character/Character_Data.txt", "w"))

    def Character_Load_Files(self):

        self.save = json.load(open("Character/Character_Data.txt"))



    def Draw(self,window):

        if self.status == "idle":
            window.blit(pygame.transform.flip(self.idle_list[self.idle_animation], self.direction, False),
                        (self.x, self.y))
        elif self.status == "idle_sword":
            window.blit(pygame.transform.flip(self.C_idle_sword_List[self.C_idle_sword_Animation], self.direction, False),
                        (self.x, self.y))
        elif self.status == "Run":
            window.blit(pygame.transform.flip(self.C_run_List[self.C_run_Animation], self.direction, False),
                        (self.x, self.y))
        elif self.status == "draw_sword":
            window.blit(pygame.transform.flip(self.C_draw_sword_List[self.C_draw_sword_Animation],
                                              self.direction, False), (self.x, self.y))
        elif self.status == "draw_sword_back":
            window.blit(pygame.transform.flip(self.C_draw_sword_back_List[self.C_draw_sword_Animation],
                                              self.direction, False), (self.x, self.y))
        elif self.status == "attack_one":
            window.blit(pygame.transform.flip(self.C_attack_one_List[self.C_attack_one_Animation],
                                              self.direction, False), (self.x, self.y))

        #pygame.draw.rect(window, (255, 0, 0), (self.x + 65, self.y + 25, 67, 120), 3)


    def Animation(self, Delay, animation_Number, limit_of_the_animation, condition=False,
                  action_mode_end=False, status_mode_end="idle"):
        if pygame.time.get_ticks() - self.time > Delay:
            animation_Number += 1
            if animation_Number == limit_of_the_animation:
                animation_Number = 0

                if condition:
                    self.action_mode = action_mode_end
                    self.status = status_mode_end
                    self.animation_mode = False


            self.time = pygame.time.get_ticks()
        return animation_Number

    def GameLoop(self, Key, Mouse):
        self.Key = Key
        self.Mouse = Mouse

        if self.Key[pygame.K_d]:
            self.status = "Run"
            self.direction = False
            self.x += self.speed
        elif self.Key[pygame.K_a]:
            self.status = "Run"
            self.direction = True
            self.x -= self.speed

        elif self.Key[pygame.K_j]:
            self.save_files()

        elif self.Key[pygame.K_r]:
            if self.action_mode == False:
                self.status = "draw_sword"
                self.animation_mode = True
            elif self.action_mode == True:
                self.status = "draw_sword_back"
                self.animation_mode = True

        elif self.Mouse[0] == 1:
            self.status = "attack_one"
            self.animation_mode = True

        else:
            if self.animation_mode == False:
                if self.action_mode == True:
                    self.status = "idle_sword"
                else:
                    self.status = "idle"



        ######## Animation #########
        if self.action_mode == False:
            if self.status == "idle":
                self.idle_animation = self.Animation(self.idle_delay,
                                                     self.idle_animation, 3)

            elif self.status == "Run":
                self.C_run_Animation = self.Animation(self.C_run_delay,
                                                      self.C_run_Animation, 6)

            elif self.status == "draw_sword":
                self.C_draw_sword_Animation = self.Animation(self.C_draw_sword_delay,
                                                             self.C_draw_sword_Animation,
                                                             4, self.animation_mode, True, "idle_sword")

            elif self.status == "attack_one":
                self.C_attack_one_Animation = self.Animation(self.C_attack_one_delay,
                                                             self.C_attack_one_Animation,
                                                             5, self.animation_mode, True, "idle_sword")

        elif self.action_mode == True:
            if self.status == "idle_sword":
                self.C_idle_sword_Animation = self.Animation(self.C_idle_sword_delay,
                                                             self.C_idle_sword_Animation,
                                                             4)
            elif self.status == "Run":
                self.C_run_Animation = self.Animation(self.C_run_delay,
                                                      self.C_run_Animation, 6)

            elif self.status == "draw_sword_back":
                self.C_draw_sword_Animation = self.Animation(self.C_draw_sword_delay,
                                                             self.C_draw_sword_Animation,
                                                             4, self.animation_mode, False, "idle")

            elif self.status == "attack_one":
                self.C_attack_one_Animation = self.Animation(self.C_attack_one_delay,
                                                             self.C_attack_one_Animation,
                                                             5, self.animation_mode, True, "idle_sword")

    def get_rect(self):
        return pygame.Rect(self.x + 65, self.y + 25, 67, 120) #x, y, width, height