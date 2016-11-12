'''
Created on May 1, 2013

@author: JC_iMac
'''

import sys, random, time, pygame, pygame.mixer, math
from pygame.locals import *
from tools import *


# Main Program
title = 'Flash Square'
pygame.init()
w,h = (600,600)
screen = pygame.display.set_mode((h,w))
screen_center = (h/2,w/2)
font1 = pygame.font.Font(None,24)
pygame.mouse.set_visible(False)
FPS = 60 
framerate = pygame.time.Clock()
keys = pygame.key.get_pressed()



while True:
    
    framerate.tick(FPS)                                                   # setting the frame rate
    milliseconds = pygame.time.get_ticks()                                # grabbing game ticks
    seconds = milliseconds / 1000                                         # changing to seconds
    pygame.display.set_caption(title+ " - %d Fps" % framerate.get_fps()) # Adding frame rate to window bar
    screen.fill(get_colours('Black'))
    
    
    
    for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
               
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()

    pygame.display.update()