#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Lab#: 12C

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab 12C")

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

square_surface = pygame.Surface((50, 50))
square_surface.fill(BLUE)
square_rect = square_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

speed = 5
clock = pygame.time.Clock()
FPS = 60
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                square_rect.center = (WIDTH // 2, HEIGHT // 2)
                print("[EVENT] KEY STATE: USER PRESSED BUTTON R -> RESETTING PLAYER POSITION")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if square_rect.top > 0:
            square_rect.y -= speed
            print("[EVENT] KEY STATE: W KEY IS BEING PRESSED -> MOVING PLAYER UP")
        else:
            print("[EVENT] KEY STATE: W KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")

    if keys[pygame.K_s]:
        if square_rect.bottom < HEIGHT:
            square_rect.y += speed
            print("[EVENT] KEY STATE: S KEY IS BEING PRESSED -> MOVING PLAYER DOWN")
        else:
            print("[EVENT] KEY STATE: S KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")

    if keys[pygame.K_a]:
        if square_rect.left > 0:
            square_rect.x -= speed
            print("[EVENT] KEY STATE: A KEY IS BEING PRESSED -> MOVING PLAYER TO THE LEFT")
        else:
            print("[EVENT] KEY STATE: A KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")

    if keys[pygame.K_d]:
        if square_rect.right < WIDTH:
            square_rect.x += speed
            print("[EVENT] KEY STATE: D KEY IS BEING PRESSED -> MOVING PLAYER TO THE RIGHT")
        else:
            print("[EVENT] KEY STATE: D KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")

    screen.blit(square_surface, square_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()