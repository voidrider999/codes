import pygame
import random

N = 50
VX_MAX = 10
VY_MAX = 10
HEIGHT = 500
WIDTH = 500
PROTECTED = 17
VISIBLE = 50
PROTECTED_COEF = 0.05
SYNC_COEF = 0.3
CENTER_COEF = 0.01
WALL_ACCEL = 2

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

class Boid:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 5)

    def wall_collision(self):
        if self.x >= WIDTH - 50:
            self.vx += -WALL_ACCEL
        if self.x <= 50:
            self.vx += WALL_ACCEL
        if self.y >= HEIGHT - 50:
            self.vy += -WALL_ACCEL
        if self.y <= 50:
            self.vy += WALL_ACCEL

    def limit_velocity(self):
        if self.vx > VX_MAX:
            self.vx = VX_MAX
        if self.vx < -VX_MAX:
            self.vx = -VX_MAX
        if self.vy > VY_MAX:
            self.vy = VY_MAX
        if self.vy < -VY_MAX:
            self.vy = -VY_MAX


boids = []
for _ in range(N):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    vx = random.randint(-VX_MAX, VX_MAX)
    vy = random.randint(-VY_MAX, VY_MAX)
    boid = Boid(x, y, vx, vy)
    boids.append(boid)

while True:
    screen.fill((0, 0, 0))
    for i in range(len(boids)):
        boid = boids[i]
        visible_avg_vx = 0
        visible_avg_vy = 0
        visible_avg_x = 0
        visible_avg_y = 0
        visible_count = 0
        for j in range(len(boids)):
            if i == j:
                continue
            other = boids[j]
            dist_x = boid.x - other.x
            dist_y = boid.y - other.y
            if abs(dist_x) <= PROTECTED and abs(dist_y) <= PROTECTED:
                boid.vx += dist_x * PROTECTED_COEF
                boid.vy += dist_y * PROTECTED_COEF
            elif abs(dist_x) <= VISIBLE and abs(dist_y) <= VISIBLE:
                visible_count += 1
                visible_avg_vx += other.vx
                visible_avg_vy += other.vy
                visible_avg_x += other.x
                visible_avg_y += other.y
            else:
                pass

        if visible_count > 0:
            visible_avg_vx /= visible_count
            visible_avg_vy /= visible_count
            boid.vx += (visible_avg_vx - boid.vx) * SYNC_COEF
            boid.vy += (visible_avg_vy - boid.vy) * SYNC_COEF

            visible_avg_x /= visible_count
            visible_avg_y /= visible_count
            dist_x = boid.x - visible_avg_x
            dist_y = boid.y - visible_avg_y
            boid.vx += -dist_x * CENTER_COEF
            boid.vy += -dist_y * CENTER_COEF

        boid.wall_collision()
        boid.limit_velocity()

        boid.update()
        boid.draw(screen)
    pygame.display.flip()
    clock.tick(60)
