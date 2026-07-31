#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 12A

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab 12A")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

small_rect = pygame.Rect(0, HEIGHT // 2 - 25, 50, 50)
small_surface = pygame.Surface((50, 50))
small_surface.fill(BLUE)

long_rect = pygame.Rect(WIDTH // 2 - 25, 0, 50, 400)
long_surface = pygame.Surface((50, 400))
long_surface.fill(RED)

velocity = 5
moving_right = True

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if moving_right:
        small_rect.x += velocity
        if small_rect.right >= WIDTH:
            moving_right = False
    else:
        small_rect.x -= velocity
        if small_rect.left <= 0:
            moving_right = True

    if small_rect.colliderect(long_rect):
        long_surface.fill(GREEN)
    else:
        long_surface.fill(RED)

    screen.blit(long_surface, long_rect)
    screen.blit(small_surface, small_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()