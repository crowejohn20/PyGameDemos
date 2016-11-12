'''
Created on 15 Oct 2012

@author: jcrowe
'''
import pygame, random, sys
from pygame.locals import *

W_WIDTH = 200
W_HEIGHT = 200
WHITE,RED = (255, 255, 255),(255,0,0)
BGCOLOR = (0, 0, 0)
FPS = 60
w_direction = 1
r_direction = 1

def terminate():
    pygame.quit()
    sys.exit()    


pygame.init()
mainClock = pygame.time.Clock()
screen_surface = pygame.display.set_mode((W_WIDTH,W_HEIGHT))
white_x,white_y = 0 ,W_HEIGHT / 2
red_x, red_y = W_WIDTH /2, W_HEIGHT -5

while True:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate(); 
    
    screen_surface.fill(BGCOLOR)
    white_rect = pygame.draw.rect(screen_surface,WHITE,(white_x,white_y,5,5),0)
    red_rect = pygame.draw.rect(screen_surface,RED,(red_x,red_y,5,5),0)
        
    white_x += w_direction
    red_y +=  r_direction
    
    if white_x > W_WIDTH or white_x < 0:
        w_direction *= -1
    
    if red_y > W_HEIGHT or red_y < 0:
        r_direction *= -1
    
    
    mainClock.tick(FPS)
    pygame.display.flip()
