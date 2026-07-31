#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 11A

import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Lab11A: Fade Background")

clock = pygame.time.Clock()

fade_value = 0
fading_to_white = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    screen.fill((fade_value, fade_value, fade_value))

    pygame.display.flip()

    if fading_to_white:
        fade_value += 1
        if fade_value >= 255:
            fade_value = 255
            fading_to_white = False
    else:
        fade_value -= 1
        if fade_value <= 0:
            fade_value = 0
            fading_to_white = True

    clock.tick(60)