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
new = {
    'xc': random.randint(5, 45),
    'yc': random.randint(5, 20),
}

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

    t = clock.tick(60) / 1000
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

        if head['xc'] > 49:
            head['xc'] = 0
        if head['xc'] < 0:
            head['xc'] = 49
        if head['yc'] > 49:
            head['yc'] = 0
        if head['yc'] < 0:
            head['yc'] = 49

        for cell in snake[:-1]:
            if head['xc'] == cell['xc'] and head['yc'] == cell['yc']:
                speed = 0
                break

        if head['xc'] == new['xc'] and head['yc'] == new['yc']:
            speed *= 1.1 
            snake.insert(0, new)
            while True:
                new = {
                    'xc': random.randint(0, 49),
                    'yc': random.randint(0, 49),
                }
                new_is_too_near = False
                for cell in snake:
                    dist_x = abs(cell['xc'] - new['xc'])
                    dist_y = abs(cell['yc'] - new['yc'])
                    if dist_x < 5 and dist_y < 5:
                        new_is_too_near = True
                        break
                if not new_is_too_near:
                    break

    print(t, dist)
    screen.fill((0, 0, 0))

    x = new['xc'] * 10
    y = new['yc'] * 10
    pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(x, y, 10, 10)) 

    for (i, cell) in enumerate(reversed(snake)):
        x = cell['xc'] * 10
        y = cell['yc'] * 10
        if i % 2 == 0:
            color = (255, 0, 0)
        else:
            color = (0, 255, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))

    pygame.display.flip()
