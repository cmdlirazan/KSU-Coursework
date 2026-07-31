#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 12B

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab 12B")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

center_rect = pygame.Rect((WIDTH // 2) - 25, 0, 50, HEIGHT)
center_surface = pygame.Surface((50, HEIGHT))
center_surface.fill(RED)

top_rect = pygame.Rect(0, 0, 50, 50)
top_surface = pygame.Surface((50, 50))
top_surface.fill(BLUE)

middle_rect = pygame.Rect(0, (HEIGHT // 2) - 25, 50, 50)
middle_surface = pygame.Surface((50, 50))
middle_surface.fill(BLUE)

bottom_rect = pygame.Rect(0, HEIGHT - 50, 50, 50)
bottom_surface = pygame.Surface((50, 50))
bottom_surface.fill(BLUE)

top_speed = 10
middle_speed = 5
bottom_speed = 20

clock = pygame.time.Clock()
FPS = 60
running = True

moving_rects = [top_rect, middle_rect, bottom_rect]

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    top_rect.x += top_speed
    middle_rect.x += middle_speed
    bottom_rect.x += bottom_speed

    if top_rect.left <= 0 or top_rect.right >= WIDTH:
        top_speed *= -1
    if middle_rect.left <= 0 or middle_rect.right >= WIDTH:
        middle_speed *= -1
    if bottom_rect.left <= 0 or bottom_rect.right >= WIDTH:
        bottom_speed *= -1

    index = center_rect.collidelist(moving_rects)
    if index != -1:
        center_surface.fill(GREEN)
    else:
        center_surface.fill(RED)

    screen.blit(center_surface, center_rect)
    screen.blit(top_surface, top_rect)
    screen.blit(middle_surface, middle_rect)
    screen.blit(bottom_surface, bottom_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()