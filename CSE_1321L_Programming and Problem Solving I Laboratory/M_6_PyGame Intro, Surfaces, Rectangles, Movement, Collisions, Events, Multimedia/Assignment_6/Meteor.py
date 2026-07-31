#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: Meteor

import pygame
import random
from Config import METEOR_IMAGES, METEOR_SPEEDS, SCREEN_WIDTH, SPAWN_SOUNDS

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(list(METEOR_IMAGES.keys()))
        self.image = pygame.image.load(random.choice(METEOR_IMAGES[self.type])).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = METEOR_SPEEDS[self.type]
        self.spawn_sound = pygame.mixer.Sound(random.choice(SPAWN_SOUNDS))

    def fall(self):
        self.rect = self.rect.move(0, self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)