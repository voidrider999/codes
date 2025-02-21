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

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

speed = 4 # cells/sec
dist = 0
direction = RIGHT
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT 
            elif event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_DOWN:
                direction = DOWN

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
        if direction == RIGHT:
            head['xc'] += 1
        elif direction == LEFT:
            head['xc'] -= 1
        elif direction == UP:
            head['yc'] -= 1
        elif direction == DOWN:
            head['yc'] += 1

    print(t, dist)
    screen.fill((0, 0, 0))
    for i, cell in enumerate(snake):
        x = cell['xc'] * 10
        y = cell['yc'] * 10
        if i % 2 == 0:
            color = (255, 0, 0)
        else:
            color = (0, 255, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
    pygame.display.flip()
