'''
Created on Feb 8, 2013

Function to help print text on screen.

Pass - Font,position_x, position_y, "String Text", colour

Returns text,(x,y) blit this to screen. 

@author: crowejohn20
'''
import math,sys,time,random, pygame
from pygame.locals import *


class Point(object):
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x
    def setx(self,x):
        self.__x = x
    x = property(getx,setx)
    
    
    def gety(self):return self.__y
    def sety(self,y): self.__y = y
    y = property(gety,sety)
    
    def __str__(self):
        return'{X:' + '{:.0f}'.format(self.__x) + \
            ',Y:' + '{:.0f}'.format(self.__y) +'}'


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # extend the base Sprite class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns =1 
        self.last_time = 0
        
    # X property
    def _getx(self):return self.rect.x
    def _setx(self, value): self.rect.x = value
    X = property(_getx,_setx)
    
    # Y property
    def _gety(self):return self.rect.y
    def _sety(self, value): self.rect.y = value
    Y = property(_gety,_sety)
    
    # position property 
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)
    
    def load(self,filename,width = 0 ,height = 0 ,columns = 1):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.set_image(self.master_image,width,height,columns)
        
    def set_image(self, image, width = 0, height = 0, columns = 1):
        self.master_image = image
        if width == 0 and height == 0:
            self.frame_width = image.get_width()
            self.frame_height = image.get_height()
        else:
            self.frame_width = width
            self.frame_height = height
            rect = self.master_image.get_rect()
            self.last_frame = (rect.width // width)*(rect.heigth // height) -1 
        self.rect = Rect(0,0,self.frame_width,self.frame_height)
        self.columns = columns

    
    def update(self, current_time, rate=30):
        # update animation frame number
        if self.last_frame > self.fist_frame:
            if current_time > self.last_time + rate:
                self.frame +=1
                if self.frame > self.last_frame:
                    self.frame = self.first_frame
                self.last_time = current_time
        
        # build current frame only if changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_height, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
    
    def __str__(self):
        return str(self.frame) + ',' + str(self.fram_width) + \
            ',' + str(self.last_frame) + ',' + str(self.frame_width) + \
            ',' + str(self.frame_height) + ',' + str(self.columns) + \
            ',' + str(self.rect)


#-----------------------------------------------------------------
def print_text(font,x,y,text,colour = (255,255,255)):
    imgText = font.render(text, True, colour)
    return(imgText,(x,y))

#----------------------------------------------------------------
def get_colours(colour):
    
    colours_aval = { 'White'  :(255,255,255),
                     'Red'    :(220,50,50),
                     'Black'  :(0,0,0),
                     'Cyan'   :(0,255,255),
                     'Yellow' :(255,255,0),
                     'Purple' :(255,0,255),
                     'Green'  :(0,255,0)   }
    
    default_colour = colours_aval['White']
    
    if colour in colours_aval:
        return(colours_aval[colour])
    
    return(default_colour)
#----------------------------------------------------------------
def get_distance(obj,player):
    
    ''' Get distance between objects '''
    
    dist_matrix = []
    
    for x in obj:
        dis_x = x[0] - player[0]
        dis_y = x[1] - player[1]
        dist_matrix.append(int(math.sqrt((dis_x) **2 + (dis_y **2))))
 
    return(dist_matrix.index(min(dist_matrix)),min(dist_matrix))
#----------------------------------------------------------------
def angular_velocity(angle):
    ''' Calculates the angular velocity ''' 
    
    vel = Point(0,0)
    vel.x = math.cos(math.radians(angle))
    vel.y = math.sin(math.radians(angle))
    return vel
#----------------------------------------------------------------
