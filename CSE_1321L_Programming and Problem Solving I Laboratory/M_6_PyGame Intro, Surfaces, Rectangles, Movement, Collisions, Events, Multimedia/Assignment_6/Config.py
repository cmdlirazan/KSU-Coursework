#Class: CSE 1321L
#Section: W07
#Term: Summer 2025
#Instructor: Ayesha Kauser Shaik
#Name: Christine Marie Lirazan
#Assignment#: Config

import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800
PLAYER_SPEED = 12
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BACKGROUND_IMAGE_PATH = "images/bg.png"
PLAYER_IMAGE_PATH = "images/player_sprite.png"

PLAYER_DEAD_SOUND = "sounds/player_dead.ogg"
SPAWN_SOUNDS = [
    "sounds/spawn_sound_1.ogg",
    "sounds/spawn_sound_2.ogg",
    "sounds/spawn_sound_3.ogg"
]

METEOR_IMAGES = {
    "big": ["images/meteor_big_1.png", "images/meteor_big_2.png", "images/meteor_big_3.png", "images/meteor_big_4.png"],
    "med": ["images/meteor_med_1.png", "images/meteor_med_2.png"],
    "small": ["images/meteor_small_1.png", "images/meteor_small_2.png"],
    "tiny": ["images/meteor_tiny_1.png", "images/meteor_tiny_2.png"]
}

METEOR_SPEEDS = {
    "big": 10,
    "med": 11,
    "small": 12,
    "tiny": 13
}

SPAWN_METEOR_EVENT = pygame.USEREVENT + 1