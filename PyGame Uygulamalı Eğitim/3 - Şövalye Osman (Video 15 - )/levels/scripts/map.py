import pygame


class Map:
    def __init__(self, level_name):
        self.level_name = level_name

        self.coin = pygame.image.load("levels/materials/coin.png")
        self.coin = pygame.transform.scale(self.coin, (60, 60))

        self.tile = open(f"levels/data/{self.level_name}/tile.txt").readlines()
        self.tile = [list(row[:-1]) for row in self.tile]

        self.map_tag_tile = "abcdefghijkl"
        self.map_tile_assets = []
        for tag in self.map_tag_tile:
            self.map_tile_assets.append(pygame.image.load(f"levels/data/{self.level_name}/{tag}.png").convert_alpha())

    def draw_map(self, window):
        for y in range(len(self.tile) - 1):
            for x in range(len(self.tile[0]) - 1):
                if self.tile[y][x] in self.map_tag_tile:
                    window.blit(self.map_tile_assets[self.map_tag_tile.index(self.tile[y][x])], (x * 32, y * 32))

    def get_coin(self, x, y):
        return [self.coin, x, y, pygame.Rect(x + 18, y + 17, 25, 25)]
