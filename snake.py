import pygame
import random

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

snake = [
    {'xc': 24, 'yc': 25},
    {'xc': 25, 'yc': 25},
    {'xc': 26, 'yc': 25},
]

while True:
    t = clock.tick(10)
    print(t)
    screen.fill((0, 0, 0))
    for cell in snake:
        x = cell['xc'] * 10
        y = cell['yc'] * 10
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x, y, 10, 10))
    pygame.display.flip()
