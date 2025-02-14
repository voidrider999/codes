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

    def move(self):
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

    def interact(self, boids):
        visible_avg_vx = 0
        visible_avg_vy = 0
        visible_avg_x = 0
        visible_avg_y = 0
        visible_count = 0
        for other in boids:
            if other is self:
                continue
            dist_x = self.x - other.x
            dist_y = self.y - other.y
            if abs(dist_x) <= PROTECTED and abs(dist_y) <= PROTECTED:
                self.vx += dist_x * PROTECTED_COEF
                self.vy += dist_y * PROTECTED_COEF
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
            self.vx += (visible_avg_vx - self.vx) * SYNC_COEF
            self.vy += (visible_avg_vy - self.vy) * SYNC_COEF

            visible_avg_x /= visible_count
            visible_avg_y /= visible_count
            dist_x = self.x - visible_avg_x
            dist_y = self.y - visible_avg_y
            self.vx += -dist_x * CENTER_COEF
            self.vy += -dist_y * CENTER_COEF


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
    for boid in boids:
        boid.interact(boids)
        boid.wall_collision()
        boid.limit_velocity()
        boid.move()
        boid.draw(screen)

    pygame.display.flip()
    clock.tick(60)
