import pygame
import random

N = 10
VX_MAX = 3
VY_MAX = 3
HEIGHT = 500
WIDTH = 500
DISTANCE = 15
DISTANCE_COEF = 0.5

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

boids = []
for _ in range(N):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    vx = random.randint(-VX_MAX, VX_MAX)
    vy = random.randint(-VY_MAX, VY_MAX)
    boid = {'x': x, 'y': y, 'vx': vx, 'vy': vy}
    boids.append(boid)

while True:
    screen.fill((0, 0, 0))
    for i in range(len(boids)):
        boid = boids[i]
        for j in range(len(boids)):
            if i == j:
                continue
            other = boids[j]
            dist_x = boid['x'] - other['x']
            dist_y = boid['y'] - other['y']
            if abs(dist_x) <= DISTANCE and abs(dist_y) <= DISTANCE:
                boid['vx'] += dist_x * DISTANCE_COEF
                boid['vy'] += dist_y * DISTANCE_COEF

        if boid['x'] >= WIDTH - 50:
            boid['vx'] -= 0.5
        if boid['x'] <= 50:
            boid['vx'] += 0.5 
        if boid['y'] >= HEIGHT - 50:
            boid['vy'] -= 0.5
        if boid['y'] <= 50:
            boid['vy'] += 0.5

        if boid['vx'] > VX_MAX:
            boid['vx'] = VX_MAX
        if boid['vx'] < -VX_MAX:
            boid['vx'] = -VX_MAX
        if boid['vy'] > VY_MAX:
            boid['vy'] = VY_MAX
        if boid['vy'] < -VY_MAX:
            boid['vy'] = -VY_MAX

        boid['x'] += boid['vx']
        boid['y'] += boid['vy']
        pygame.draw.circle(screen, (255, 0, 0), (boid['x'], boid['y']), 5)
    pygame.display.flip()
    clock.tick(60)
