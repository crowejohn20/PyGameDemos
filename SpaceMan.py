#!/usr/local/Cellar/python3/3.5.2_3/bin/python3
import random
import pygame
import os

WIDTH = 640
HEIGHT = 480
FPS = 30

WHITE   = (255,255,255)
RED     = (220,50,50)
BLACK   = (0,0,0)
CYAN    = (0,255,255)
YELLOW  = (255,255,0)
PURPLE  = (255,0,255)
GREEN   = (0,255,0)

# set up assets
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"Artwork")

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)

        # Grab image and create a rect
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH /2, HEIGHT /2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed

        if self.rect.bottom > HEIGHT - 100:
            self.y_speed = - 5
        if self.rect.top < 100:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


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
    all_sprites.update()


    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # Draw then flip to update screen
    pygame.display.flip()

pygame.quit()
