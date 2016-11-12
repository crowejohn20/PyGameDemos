'''
Created on 18 Oct 2012

@author: jcrowe
'''
import sys, random, time, pygame, math
from pygame.locals import *
from print_text import *

x = y = 0
tile_size = 32
s_WIDTH = 640
s_HEIGHT = 480

x_center = s_WIDTH/2
y_center = s_HEIGHT/2

x_tile = int(s_WIDTH / tile_size) 
y_tile = int(s_HEIGHT / tile_size)

tile_store = [0]*(32 *32) 
line = []
pygame.init()
font1 = pygame.font.Font(None,24)
running = True
screen_base = pygame.display.set_mode((s_WIDTH,s_HEIGHT))
color = (255,255,225)



def draw_coords(cc):
    
    coor = print_text(font1,200,200,'Cartesian Coordinates:'+ str(cc))
    screen_base.blit(coor[0],coor[1])
    print(coor)
    
    

while running:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            line.append(event.pos)
            if len(line) >=2:
                
                pos_x = line[0][0] - line[1][0]
                pos_y = line[0][1] - line[1][1]
                
                dist = math.sqrt((pos_x) **2 + (pos_y **2))
                draw_coords(dist)
                
                
                pygame.draw.line(screen_base,(color),(line[0]),(line[1]),5)
                line = []
            
            cc = event.pos[0] - x_center, event.pos[1] - y_center
            from_center = (int(x_center + y_center) - (event.pos[0] + event.pos[1]))
            tile_coor = (int(event.pos[0] / x_tile)+1, int(event.pos[1] / y_tile )+1)
            tile_num = (tile_coor[1] * tile_size) - (tile_size - tile_coor[0])
            
            
            
            #print('Cartesian Coordinates:',str(cc))
            #print('Tile Coordinates:', str(tile_coor))
            #print('Tile Number:', tile_num)
            #print('Length from center', from_center)
            #print('Distance \n')
            
            if cc[0] > 0 and cc[1] < 0:
                color = (0,0,255)
                print('Section 1')
            elif cc[0] < 0 and cc[1] < 0:
                color = (255,255,255)
                print('Section 2')
            elif cc[0] < 0 and cc[1] > 0:
                color = (255,0,255)
                print('Section 3')
            elif cc[0] > 0 and cc[1] > 0:
                color = (200,200,255)
                print('Section 4')
            
            #pygame.draw.rect(screen_base,(255,255,255),(event.pos[0],event.pos[1],16,12),0)
            #pygame.draw.rect(screen_surface,WHITE,(white_x,white_y,5,5),0)
            
        for x in range(0,tile_size):
            pygame.draw.line(screen_base,(0,50,10),(x_tile * x,0),(x_tile *x,s_HEIGHT))
            pygame.draw.line(screen_base,(0,50,10),(0,y_tile * x),(s_WIDTH,y_tile *x))
        
        pygame.draw.line(screen_base,(255,255,255),(0,y_center),(s_WIDTH,y_center))
        pygame.draw.line(screen_base,(255,0,0),(x_center,0),(x_center,s_HEIGHT))
        pygame.display.flip()
