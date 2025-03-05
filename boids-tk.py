import pygame
import random
import tkinter as tk
from tkinter import ttk

N = 50
VX_MAX = 10
VY_MAX = 10
HEIGHT = 500
WIDTH = 500
PROTECTED = 17
VISIBLE = 50
separation_coef = 0.05
sync_coef = 0.3
center_coef = 0.01
wall_coef = 2

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

def show_gui():
    root = tk.Tk()
    root.geometry("250x200")
    root.eval('tk::PlaceWindow . center')

    label = ttk.Label(text='Wall Repulsion')
    label.pack()
    wall_spin = ttk.Spinbox(from_=0, to=5, increment=0.1)
    wall_spin.set(wall_coef)
    wall_spin.pack()

    label = ttk.Label(text='Separation')
    label.pack()
    separation_spin = ttk.Spinbox(from_=0, to=0.5, increment=0.01)
    separation_spin.set(separation_coef)
    separation_spin.pack()

    label = ttk.Label(text='Synchronicity of speed')
    label.pack()
    sync_spin = ttk.Spinbox(from_=0, to=0.5, increment=0.01)
    sync_spin.set(sync_coef)
    sync_spin.pack()

    label = ttk.Label(text='Centering')
    label.pack()
    center_spin = ttk.Spinbox(from_=0, to=0.5, increment=0.01)
    center_spin.set(center_coef)
    center_spin.pack()

    def apply():
        global wall_coef
        wall_coef = float(wall_spin.get())
        global separation_coef
        separation_coef = float(separation_spin.get())
        global sync_coef
        sync_coef = float(sync_spin.get())
        global center_coef
        center_coef = float(center_spin.get())
        root.destroy()

    okay = ttk.Button(text='OK', command=apply)
    okay.pack()

    root.mainloop()

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F2:
                show_gui()

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
            dist_x = boid['x'] - other['x']
            dist_y = boid['y'] - other['y']
            if abs(dist_x) <= PROTECTED and abs(dist_y) <= PROTECTED:
                boid['vx'] += dist_x * separation_coef
                boid['vy'] += dist_y * separation_coef
            elif abs(dist_x) <= VISIBLE and abs(dist_y) <= VISIBLE:
                visible_count += 1
                visible_avg_vx += other['vx']
                visible_avg_vy += other['vy']
                visible_avg_x += other['x']
                visible_avg_y += other['y']
            else:
                pass

        if visible_count > 0:
            visible_avg_vx /= visible_count
            visible_avg_vy /= visible_count
            boid['vx'] += (visible_avg_vx - boid['vx']) * sync_coef
            boid['vy'] += (visible_avg_vy - boid['vy']) * sync_coef

            visible_avg_x /= visible_count
            visible_avg_y /= visible_count
            dist_x = boid['x'] - visible_avg_x
            dist_y = boid['y'] - visible_avg_y
            boid['vx'] += -dist_x * center_coef
            boid['vy'] += -dist_y * center_coef

        if boid['x'] >= WIDTH - 50:
            boid['vx'] -= wall_coef
        if boid['x'] <= 50:
            boid['vx'] += wall_coef
        if boid['y'] >= HEIGHT - 50:
            boid['vy'] -= wall_coef
        if boid['y'] <= 50:
            boid['vy'] += wall_coef

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
