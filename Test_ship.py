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

        for star in range(0,50):
            pos_x  = random.randint(0,h)
            pos_y  = random.randint(0,w)
            vel_y  = random.randint(1,10)
            star_size   = vel_y
            
            pos = [pos_x,pos_y,vel_y,star_size]
            self.stars.append(pos)
    
    def move_stars(self, direction):
        
        for star_pos in self.stars:
            star_pos[1] += star_pos[2]
            
            if direction == 'R':
                star_pos[0] -= 1
            elif direction == 'L':
                star_pos[0] += 1
            
            elif direction == 'UP':
                star_pos[1] += 5
                
            
            elif direction == 'BACK':
                star_pos[1] -= 1
                
            if star_pos[1] > h:
                star_pos[1] = (h -h -1)
                                    
            pygame.draw.rect(screen, get_colours('Red'),(star_pos[0],star_pos[1],star_pos[2],star_pos[2]),0)        

            
class star_ship(object):
    def __init__(self):
        
        self.health = 100
        self.lives  = 3
        self.ship_x = w/2 -50
        self.ship_y = h-50
        self.left = 0
        self.right = 1
        self.forward = 10
        self.max_forward = h/3
        
        self.bullet_x = self.ship_x
        self.bullet_y = self.ship_y
        self.bullet_size_x = 2
        self.bullet_size_y = 3
        self.bullet_speed = 10
        self.bullets = []
        
    
    def move_ship(self):
        ''' '''
    
    def ship_fire(self,pos_x,pos_y):
        
        track = [pos_x,pos_y]
        self.bullets.append(track)
        
        for i in self.bullets:
            i[1] += self.bullet_speed
            
        
        
        
        
        
        

class main_menu(object):
    
    def __init__(self,mouse_x,mouse_y,menu_h,menu_w):
        
        self.menu_h = menu_h
        self.menu_w = menu_w
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.center_y = menu_h/2
        self.center_x = menu_w/2
        self.menu_size = 400,200
    
    def draw_menu(self):
        
        main_menu = pygame.Rect(0,0,500,500)
        main_menu_w = main_menu[2]
        main_menu_h = main_menu[3]
        main_menu_x = self.center_x - main_menu.centerx
        main_menu_y = self.center_y - main_menu.centery
        
        
        srt_game_btn = pygame.Rect(0,0,100,100)
        srt_game_center = self.center_x - srt_game_btn[2]
        srt_text_center = self.center_x -srt_game_btn.centerx 
        
        start_btn = pygame.sprite.Sprite()
        start_btn.image = pygame.image.load('start.png')
        start_btn.rect = start_btn.image.get_rect()
        start_btn.center = start_btn.image.get_rect().center
        start_btn.rect[0] = self.center_x - start_btn.center[0]
        start_btn.rect[1] = self.center_y - start_btn.center[1]
        
        start_objs = (start_btn.image,start_btn.rect)
        start_pos  = (self.center_x - start_btn.center[0],self.center_y - start_btn.center[1])
       
        pygame.draw.line(screen,get_colours('Red'),(main_menu_x,10),(main_menu_w + main_menu_x,10),2)
        pygame.draw.rect(screen,get_colours('Red'),(main_menu_x, main_menu_y,main_menu_w,main_menu_h),4)
        
        
        
        if start_objs[1].collidepoint(pygame.mouse.get_pos()):
            foo = pygame.transform.scale(start_objs[0],(100,50))
            screen.blit(foo,start_pos)
        else:
            screen.blit(start_objs[0],start_pos)
        
        
        return(start_objs)
        
        
    def menu_events(self, start_pos):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            
            #if  start_objs[1].collidepoint(pygame.mouse.get_pos()):
            #    print('Hello')
            
        else:
            return
        
        #pygame.draw.rect(screen,get_colours('Red'),(srt_game_center,main_menu_y,200,50),0)
        #print_text(font1,srt_text_center,main_menu_y,'Start Game')
        #print_text(font1, main_menu_x, 20 ,'Results')
        #print_text(font1, 300 -125,300 +5  ,'Core Dump - Segmentation fault')
        
       

def print_text(font,x,y,text,colour = (255,255,255)):
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
screen_center = (h/2,w/2)
font1 = pygame.font.Font(None,24)


pygame.mouse.set_visible(True)
clock = pygame.time.Clock()
game_over = True
key_flag = False
mouse_x = mouse_y = 0
star_objs = star_field()
ship = star_ship()
menu = main_menu(mouse_x,mouse_y,w,h)
ship_default_y = ship.ship_y
last_key = []

# Repeating event loop
while True:
    clock.tick(60)
    screen.fill(get_colours('Black'))
    pygame.display.set_caption("Core Dump - %d Fps" % clock.get_fps())
    direction = ''
    keys = pygame.key.get_pressed()
    
    
    if game_over:
        start_pos = menu.draw_menu()
        
    
    else:
    
        if keys[pygame.K_RIGHT]:
            ship.ship_x += 10
            direction = 'R'
        
        if keys[pygame.K_LEFT]:
            ship.ship_x += -10
            direction ='L'
        
        if keys[pygame.K_UP]:
            direction = 'UP'
            if ship.ship_y != 150:
                ship.ship_y -= 5
                ship.bullet_speed + 5
                key_flag = False
        
        if key_flag == True:
            if ship.ship_y < ship_default_y:
                direction = 'BACK'
                ship.ship_y +=10
        
        if keys[pygame.K_SPACE]:
            shot = [ship.ship_x +25 ,ship.ship_y,ship.bullet_speed]
            ship.bullets.append(shot)
        
        
        star_objs.move_stars(direction)
        pygame.draw.rect(screen,get_colours('Purple'),(ship.ship_x, ship.ship_y, 50, 50),0)  
            
        for idx,x in enumerate(ship.bullets):
            if x[1] < 0:
                del ship.bullets[idx]
            else:
                x[1] -= x[2]
                pygame.draw.rect(screen,get_colours('White'),(x[0],x[1],ship.bullet_size_x,ship.bullet_size_y ),0)
            
            print(idx)
            
           
            
 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        
        elif event.type == KEYUP:
            key_flag = True
           
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        
        elif event.type == KEYDOWN and event.key == K_RETURN:
            game_over = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_over == True:
                if  start_pos[1].collidepoint(pygame.mouse.get_pos()):
                    game_over = False
                

    pygame.display.update()
    
    
        
    
