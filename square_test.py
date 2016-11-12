'''
Created on Feb 6, 2013

Creating spinning squares 

@author: crowejohn20
'''


import sys, random, time, pygame
from pygame.locals import *

def print_text(font,x,y,text,colour = (255,255,255)):
    imgText = font.render(text, True, colour)
    screen.blit(imgText,(x,y))

pygame.init()
w = 400
h = 400

FPS = 60
framerate = pygame.time.Clock()



screen = pygame.display.set_mode((h,w), pygame.HWSURFACE )
screen_center = (h/2,w/2)
font_1 = pygame.font.Font(None,24)
pygame.key.set_repeat(50,50) 
pygame.mouse.set_visible(True)
mouse_x = mouse_y = 0

while True:
    screen.fill((0,0,0))
    framerate.tick(FPS)
    milliseconds = pygame.time.get_ticks()
    seconds = milliseconds / 1000 
    print_text(font_1,0,0,'seconds: ' + str(seconds))
    
    pygame.display.update()