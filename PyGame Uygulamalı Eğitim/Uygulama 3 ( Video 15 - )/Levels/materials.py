import pygame


def get_coin(x, y):
    coin = pygame.image.load("Levels/Materials/coin.png")
    coin = pygame.transform.scale(coin, (60, 60))
    return [x, y, coin, pygame.Rect(x + 15, y + 15, 30, 30)]
