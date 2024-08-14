import pygame
import pymunk
import pymunk.pygame_util
import random

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 1000)
draw_opts = pymunk.pygame_util.DrawOptions(screen)

line1 = pymunk.Segment(space.static_body, (0, 0), (140, 480), 2)
line1.elasticity = 1
line1.friction = 1
space.add(line1)

line2 = pymunk.Segment(space.static_body, (140, 480), (180, 485), 2)
line2.elasticity = 2
line2.friction = 1
space.add(line2)

line3 = pymunk.Segment(space.static_body, (200, 400), (300, 405), 2)
line2.elasticity = 0.6
line2.friction = 1
space.add(line3)

line4 = pymunk.Segment(space.static_body, (300, 500), (450, 500), 2)
line4.elasticity = 2
line4.friction = 1
space.add(line4)

i = 0
while True:
    if i % 15 == 0:
        body = pymunk.Body()
        body.position = (5, 0)     
        shape = pymunk.Circle(body, 10)
        shape.mass = 1            
        shape.elasticity = 1
        shape.friction = 1       
        space.add(body, shape)

    space.step(1/60)
    screen.fill((0, 0, 0))
    space.debug_draw(draw_opts)
    pygame.display.flip()
    clock.tick(60)
    i += 1
