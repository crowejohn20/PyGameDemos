'''
Created on Jan 4, 2013

Game where stars fall each star is a difference size and so does a different amount of damage to the ground.
Aim - the aim of the game is to catch the stars to avoid them hitting the ground

@author: crowejohn20
'''
import sys, random, time, pygame
from pygame.locals import *


class star_field(object):
    def __init__(self):
        
        self.stars = []
        
        
        for star in range(0,100):
            pos_x  = random.randint(0,h)
            pos_y  = random.randint(0,w)
            vel_y  = random.randint(1,10)
            
            pos = [pos_x,pos_y,vel_y]
            self.stars.append(pos)
    
    
    def move_stars(self, ship_pos, direction):
        
        
        for star_pos in self.stars:
        
            star_pos[1] += star_pos[2]
            
            if direction == 'R':
                star_pos[0] -= 1
            elif direction == 'L':
                star_pos[0] += 1
                
            if star_pos[1] > h:
                star_pos[1] = (-5)
                                    
            pygame.draw.rect(screen, get_colours('Red'),(star_pos[0],star_pos[1],star_pos[2],star_pos[2]),0)
            

            
class star_ship(object):
    def __init__(self):
        
        self.health = 100
        self.lives  = 3
        self.ship_x = w/2 -50
        self.ship_y = h-50
        
        

def print_text(font,x,y,text,colour =(255,255,255)):
    imgText = font.render(text, True, colour)
    screen.blit(imgText,(x,y))

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


# Main Program
pygame.init()
w = 600
h = 600
screen = pygame.display.set_mode((h,w))

font1 = pygame.font.Font(None,24)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

lives = 3
score = 0
game_over = True
mouse_x = mouse_y = 0
star_objs = star_field()
ship = star_ship()

# Repeating event loop
while True:
    clock.tick(60)
    screen.fill(get_colours('Black'))
    pygame.display.set_caption("Core Dump - %d Fps" % clock.get_fps())
    
    direction = ''
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        ship.ship_x += 10
        direction = 'R'
    
    elif keys[pygame.K_LEFT]:
        ship.ship_x += -10
        direction ='L'

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        
    
    star_objs.move_stars(ship.ship_x,direction)
    pygame.draw.rect(screen,get_colours('Purple'),(ship.ship_x, ship.ship_y, 100, 20),0)
    pygame.display.flip()
    
    #if game_over:
    #    print_text(font1,100,200,'< CLICK TO PLAY >')
    #else:
        
    

        #pygame.draw.rect(screen, get_colours('Red'),(x[0],x[1],x[2],x[2]),0)
#            direction = change_direction = move_objects(star_objs.stars,direction)

    #pygame.draw.rect(screen,get_colours('Yellow'),(w/2 -200,h/2 -100 ,400,200),4)
    #pygame.draw.rect(screen,get_colours('Black'),(w/2 -200,h/2 -100 ,400,200),0)
    
        
    
    #pygame.draw.line(screen,get_colours('Yellow'),(0,h/2),(h,w/2),2)
    #print_text(font1,w/2 -25, h/2 -25 ,'Results')
    #print_text(font1,w/2 -125, h/2 +5  ,'Core Dump - Segmentation fault')
    
    
        
    
