import pygame
import random

N = 50
VX_MAX = 10
VY_MAX = 10
HEIGHT = 500
WIDTH = 500
PROTECTED = 15
VISIBLE = 30
PROTECTED_COEF = 0.9
SYNC_COEF = 0.9
WALL_COEF = 2

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
        visible_avg_vx = 0
        visible_avg_vy = 0
        visible_count = 0
        for j in range(len(boids)):
            if i == j:
                continue
            other = boids[j]
            dist_x = boid['x'] - other['x']
            dist_y = boid['y'] - other['y']
            if abs(dist_x) <= PROTECTED and abs(dist_y) <= PROTECTED:
                boid['vx'] += dist_x * PROTECTED_COEF
                boid['vy'] += dist_y * PROTECTED_COEF
            elif abs(dist_x) <= VISIBLE and abs(dist_y) <= VISIBLE:
                visible_count += 1
                visible_avg_vx += other['vx']
                visible_avg_vy += other['vy']
            else:
                pass

        if visible_count > 0:
            visible_avg_vx /= visible_count
            visible_avg_vy /= visible_count
            boid['vx'] += (visible_avg_vx - boid['vx']) * SYNC_COEF
            boid['vy'] += (visible_avg_vy - boid['vy']) * SYNC_COEF

        if boid['x'] >= WIDTH - 50:
            boid['vx'] -= WALL_COEF
        if boid['x'] <= 50:
            boid['vx'] += WALL_COEF
        if boid['y'] >= HEIGHT - 50:
            boid['vy'] -= WALL_COEF
        if boid['y'] <= 50:
            boid['vy'] += WALL_COEF

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
