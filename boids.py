import pygame
import random

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

n = 10
boids = []
for i in range(n):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    vx = random.randint(-5, 5)
    vy = random.randint(-5, 5)
    boid = {'x': x, 'y': y, 'vx': vx, 'vy': vy}
    boids.append(boid)

while True:
    screen.fill((0, 0, 0))
    for boid in boids:
        pygame.draw.circle(screen, (255, 0, 0), (boid['x'], boid['y']), 5)
        if boid['x'] >= 450:
            boid['vx'] -= 0.5
        if boid['x'] <= 50:
            boid['vx'] += 0.5 
        if boid['y'] >= 450:
            boid['vy'] -= 0.5
        if boid['y'] <= 50:
            boid['vy'] += 0.5

        if boid['vx'] > 5:
            boid['vx'] = 5
        if boid['vx'] < -5:
            boid['vx'] = -5
        if boid['vy'] > 5:
            boid['vy'] = 5
        if boid['vy'] < -5:
            boid['vy'] = -5

        boid['x'] += boid['vx']
        boid['y'] += boid['vy']
    pygame.display.flip()
    clock.tick(60)
