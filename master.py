import pygame
from classes.drop import Drop
from random import randint


pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 800
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

drops = []

tick = 0
angle = 275
vel = 80
run = True
while run:
    tick += 1
    clock.tick(60)
    if pygame.QUIT in [event.type for event in pygame.event.get()]:
        run = False

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        angle -= 1
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        angle += 1
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        vel += 1
    if pygame.key.get_pressed()[pygame.K_UP]:
        vel -= 1

    for i in range(5):
        drops.append(Drop(pos=(None, None), angle=angle, vel=vel, color=(183, 52, 235)))

    for i, drop in enumerate(drops):
        drop.move()
        drop.set_vel(vel)
        if drop.dead:
            drops.pop(i)

    if True:
        win.fill((230, 166, 255))

        for drop in drops:
            drop.draw(win)

        pygame.display.flip()
    print(len(drops))
