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

speed = 1 # cells/sec
dist = 0
while True:
    t = clock.tick(10) / 1000
    dist += t * speed
    if dist >= 1:
        dist -= 1
        for i in range(0, len(snake) - 1):
            cell = snake[i]
            nxt = snake[i + 1]
            cell['xc'] = nxt['xc']
            cell['yc'] = nxt['yc']
        
        head = snake[-1]
        head['xc'] += 1

    print(t, dist)
    screen.fill((0, 0, 0))
    for i, cell in enumerate(snake):
        x = cell['xc'] * 10
        y = cell['yc'] * 10
        if i % 2 == 0:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
    pygame.display.flip()
