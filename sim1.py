import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 1000)
draw_opts = pymunk.pygame_util.DrawOptions(screen)

body = pymunk.Body()
body.position = (51, 0)
shape = pymunk.Circle(body, 20)
shape.mass = 1
shape.elasticity = 0.7
shape.friction = 1
space.add(body, shape)

line1 = pymunk.Segment(space.static_body, (50, 100), (200, 200), 2)
line1.elasticity = 0.7
line1.friction = 1
space.add(line1)

line2 = pymunk.Segment(space.static_body, (230, 300), (500, 100), 2)
line2.elasticity = 0.7
line2.friction = 1
space.add(line2)

line3 = pymunk.Segment(space.static_body, (0, 500), (500, 400), 2)
line2.elasticity = 0.7
line2.friction = 1
space.add(line3)

line4 = pymunk.Segment(space.static_body, (0, 300), (200, 400), 2)
line4.elasticity = 0.7
line4.friction = 1
space.add(line4)

stop_line1 = pymunk.Segment(space.static_body, (0, 500), (0, 450), 2)
stop_line1.elasticity = 0.7
stop_line1.friction = 1
space.add(stop_line1)

while True:
    space.step(1/60)
    screen.fill((0, 0, 0))
    space.debug_draw(draw_opts)
    pygame.display.flip()
    clock.tick(60)
