#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: 6

import pygame
import random
from Config import *
from Player import Player
from Meteor import Meteor

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Meteor Dodge")
clock = pygame.time.Clock()

background = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
font = pygame.font.SysFont(None, 72)

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20)
meteors = []

pygame.time.set_timer(SPAWN_METEOR_EVENT, 1000)

def draw_game_over():
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(100)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    text = font.render("You Lost!", True, WHITE)
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, rect)

running = True
while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_METEOR_EVENT:
            meteor = Meteor()
            meteors.append(meteor)
            meteor.spawn_sound.play()
            pygame.time.set_timer(SPAWN_METEOR_EVENT, random.randint(800, 1500))

    screen.blit(background, (0, 0))

    if player.alive:
        player.move(keys)
        player.draw(screen)

        for meteor in meteors[:]:
            meteor.fall()
            meteor.draw(screen)
            if meteor.rect.top > SCREEN_HEIGHT + 20:
                meteors.remove(meteor)
            elif meteor.rect.colliderect(player.rect):
                pygame.mixer.Sound(PLAYER_DEAD_SOUND).play()
                player.alive = False
                meteors.remove(meteor)
    else:
        draw_game_over()

    pygame.display.flip()

pygame.quit()