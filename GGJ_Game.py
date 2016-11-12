'''
Created on Jan 25, 2013

Simple game - The player moves around the screen and has to find the location of the sound (heartbeat) once located
a new level loads.

@author: crowejohn20
'''
import sys, random, time, pygame, pygame.mixer, math
from pygame.locals import *
from print_text import *


class player(object):
    def __init__(self):
        
        iSize_x = 25        # Length of squares x
        iSize_y = 25        # Length of squares y
        iCen_x = iSize_x/2  # Find the middle of length x
        iCen_y = iSize_y/2  # Find the middle of length y
        
        self.iSpeed = 5
        self.tPlayer_obj = pygame.Rect(0,0,iSize_x,iSize_y)
        self.tPlayer_cen = iCen_x,iCen_y
            
        
          
    def draw_move(self,event):
        
        if event[pygame.K_UP]:
            self.tPlayer_obj[1] -= self.iSpeed
        
        if event[pygame.K_DOWN]:
            self.tPlayer_obj[1] += self.iSpeed
            
        if event[pygame.K_LEFT]: 
            self.tPlayer_obj[0] -= self.iSpeed
        
        if event[pygame.K_RIGHT]:
            self.tPlayer_obj[0] += self.iSpeed
        

class goal(object):
    def __init__(self):
        
        iNum_objs = 4
        self.lScreen_objs = []
        
        for objs in range(iNum_objs):
        
            obj_pos_x = random.randint(10, w - 10)
            obj_pos_y = random.randint(10, h - 10)
            
            obj_size_x = random.randrange(5,25,5)
            obj_size_y = obj_size_x
            
            obj_cen_x = obj_size_x/2
            obj_cen_y = obj_size_y/2
            tObjects = (pygame.Rect(0,0,obj_size_x,obj_size_y),obj_pos_x,obj_pos_y)
        
            self.lScreen_objs.append(tObjects)
        


def get_distance(obj,player):
    
    ''' Get distance between objects '''
    
    dis_x = obj[0] - player[0]
    dis_y = obj[1] - player[1]
    distance = int(math.sqrt((dis_x) **2 + (dis_y **2)))
    
    return distance


# Main Program
pygame.init()
#sound = pygame.mixer.Sound('heart.wav')

w,h = (600,600)
screen = pygame.display.set_mode((h,w))
screen_center = (h/2,w/2)
font1 = pygame.font.Font(None,24)
pygame.mouse.set_visible(True)
FPS = 60 
framerate = pygame.time.Clock()

count = 0
score = 0

game_over = False
found = False
new_player = player()
new_goal = goal()


# Repeating event loop
while True:
    
    framerate.tick(FPS)                                                   # setting the frame rate
    milliseconds = pygame.time.get_ticks()                                # grabbing game ticks
    seconds = milliseconds / 1000                                         # changing to seconds
    pygame.display.set_caption("GGJ Game - %d Fps" % framerate.get_fps()) # Adding frame rate to window bar
    screen.fill(get_colours('Black'))                                     # Flash black to wipe the screen before update with below code. 
    
    keys = pygame.key.get_pressed()
    new_player.draw_move(keys)
    #distance = get_distance(new_goal.object,new_player.tPlayer_obj)
    
    timer = print_text(font1,9,560, 'Timer: ' + str(seconds))
    screen.blit(timer[0],timer[1])
    
    play_score = print_text(font1,10,540,'Score: ' + str(score))
    screen.blit(play_score[0],play_score[1])
    
    #new_dis = print_text(font1,10,580,'Distance: ' + str(distance))
    #screen.blit(new_dis[0],new_dis[1])
    
    pygame.draw.rect(screen,get_colours('Purple'),(new_player.tPlayer_obj),0)
    print(new_goal.lScreen_objs)
    #pygame.draw.rect(screen,get_colours('Red'),(new_goal.object),0)
    
    #pygame.draw.aaline(screen,(255,255,255),(new_goal.object[0] + new_goal.obj_cen_x,new_goal.object[1] + new_goal.obj_cen_y),
    #                   (new_player.tPlayer_obj[0] + new_player.tPlayer_cen[0], new_player.tPlayer_obj[1] + new_player.tPlayer_cen[1]),10)
    
    if game_over:
        print_text(font1,h/2,w/2,'Game Over')
        
    else:   
            
        #if new_player.tPlayer_obj.colliderect(new_goal.object):   
        #    found = True
        #    score +=1
        
        if found == True:
            new_goal = goal()
            found = False
            timer = 10
            

    for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            
            elif event.type == KEYUP:
                key_flag = True
               
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()

    pygame.display.update()