#!/usr/local/Cellar/python3/3.5.2_3/bin/python3
import random
import pygame

WIDTH = 640
HEIGHT = 480
FPS = 30

WHITE = (255,255,255)

# initialize pygame and creat window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Game Loop
running = True
while running:
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False
            
    # Update


    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # Draw then flip to update screen
    pygame.display.flip()

pygame.quit()
