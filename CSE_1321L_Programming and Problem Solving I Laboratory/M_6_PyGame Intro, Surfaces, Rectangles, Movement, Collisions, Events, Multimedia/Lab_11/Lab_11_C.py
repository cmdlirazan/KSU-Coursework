#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 11C

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab11C: Moving Squares")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SQUARE_SIZE = 100
SPEED = 5

top_square = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
bottom_square = pygame.Rect(0, HEIGHT - SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

direction = 1

clock = pygame.time.Clock()

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    movement = SPEED * direction
    top_square = top_square.move(movement, 0)
    bottom_square = bottom_square.move(movement, 0)

    if top_square.right >= WIDTH or top_square.left <= 0:
        direction *= -1

    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, top_square)
    pygame.draw.rect(screen, BLUE, bottom_square)
    pygame.display.flip()

    clock.tick(60)