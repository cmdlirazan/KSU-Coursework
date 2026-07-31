#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 11B

import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (600, 600)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Lab11B: Five Squares")

clock = pygame.time.Clock()

square_size = 60
square_color = (255, 0, 0)
background_color = (0, 0, 0)

square_surf = pygame.Surface((square_size, square_size))
square_surf.fill(square_color)

positions = [
    (0, 0),
    (resolution[0] - square_size, 0),
    (0, resolution[1] - square_size),
    (resolution[0] - square_size, resolution[1] - square_size),
    ((resolution[0] - square_size) // 2, (resolution[1] - square_size) // 2),
]

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    screen.fill(background_color)

    for pos in positions:
        screen.blit(square_surf, pos)

    pygame.display.flip()
    clock.tick(60)