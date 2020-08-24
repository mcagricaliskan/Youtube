import pygame

pygame.init()


class Core:
    def __init__(self):
        self.window_width = 1280
        self.window_height = 720
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Şablon")
        self.clock = pygame.time.Clock()

    def draw(self):

        self.clock.tick(60)
        pygame.display.update()

    def game_loop(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_ESCAPE]:
            return 0

        self.draw()


game = Core()

while True:
    game_status = game.game_loop()
    if game_status is not None:
        break

pygame.quit()

