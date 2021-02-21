import pygame
from pygame import Vector2
from Wall import *

import P, R

displayW = 800
displayH = 600

display = pygame.display.set_mode((displayW, displayH))
wall1 = Wall(600, 120, 600, 380)
wall2 = Wall(700, 200,700, 580)
wall3 = Wall(700, 0, 700, 400)
wall4 = Wall(500, 40, 500, 300)
wall5 = Wall(120, 120, 120, 300)
wall6 = Wall(3, 3, 797, 3)
wall7 = Wall(3, 3, 3, 597)
wall8 = Wall(3, 597, 797, 597)
wall9 = Wall(797, 597, 797, 3)
walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9]
x = 400
y = 300
vel = 7
Particles = P.Particle(x, y)
def draw(keyPressed):
    global x, y, Particles
    display.fill((0, 0, 0))
    if(keyPressed[pygame.K_w]):
        y -= vel
        Particles = P.Particle(x, y)
    if(keyPressed[pygame.K_s]):
        y += vel
        Particles = P.Particle(x, y)
    if(keyPressed[pygame.K_a]):
        x -= vel
        Particles = P.Particle(x, y)
    if(keyPressed[pygame.K_d]):
        x += vel
        Particles = P.Particle(x, y)

    for wall in walls:
        wall.show(display)


    Particles.Cast(walls, display)
    pygame.display.flip()

run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keyPressed = pygame.key.get_pressed()
    draw(keyPressed)

pygame.quit()
