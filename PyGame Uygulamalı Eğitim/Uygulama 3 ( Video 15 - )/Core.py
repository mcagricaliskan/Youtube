import pygame
import sys
from Levels.Test_Level import TestLevel
from Levels.Test_Level_Night import TestLevelNight
sys.path.append("/")


pygame.init()


class Core:
    def __init__(self):
        self.window_width = 1600
        self.window_height = 900
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Şövalye Osman")

        self.level_lock = "Test_Level"
        self.level_update()

        self.game_clock = pygame.time.Clock()

    def draw(self):

        self.current_level.draw(self.window)
        self.game_clock.tick(60)
        pygame.display.update()

    def level_update(self):

        if self.level_lock == "Test_Level":
            self.current_level = TestLevel(self.window_width, self.window_height)
        elif self.level_lock == "Test_Level_Night":
            self.current_level = TestLevelNight(self.window_width, self.window_height)

        self.level_lock = None

    def game_loop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_ESCAPE]:
            return "QUIT"

        self.mouse = pygame.mouse.get_pressed()

        self.level_lock = self.current_level.game_loop(self.key, self.mouse)

        if self.level_lock is not None:
            self.level_update()

        self.draw()


game = Core()

while True:
    Status = game.game_loop()
    if Status == "QUIT":
        break

pygame.quit()
