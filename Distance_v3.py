#!/usr/local/bin/python3
'''
Created on Jan 25, 2013
@author: crowejohn20
'''
import sys, random, time, pygame, pygame.mixer, math
from pygame.locals import *
from tools import *

TITLE = 'Distance Demo'
W,H = (600,600)
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self):
        #pygame.sprite.Sprite.__init__(self)

        iSize_x = 25
        iSize_y = 25
        iCen_x = iSize_x/2
        iCen_y = iSize_y/2

        self.iSpeed = 5
        self.tPlayer_obj = pygame.Rect(H/2,W/2,iSize_x,iSize_y)
        self.tPlayer_cen = iCen_x,iCen_y

    def update_player(self,event):

        if event[pygame.K_UP]:
            self.tPlayer_obj[1] -= self.iSpeed

        if event[pygame.K_DOWN]:
            self.tPlayer_obj[1] += self.iSpeed

        if event[pygame.K_LEFT]:
            self.tPlayer_obj[0] -= self.iSpeed

        if event[pygame.K_RIGHT]:
            self.tPlayer_obj[0] += self.iSpeed

    def draw_player(self):
        pygame.draw.rect(screen,get_colours('Purple'),(self.tPlayer_obj),0)

class Goal(object):
    def __init__(self):

        iNum_objs = 4
        self.lScreen_objs = []

        for objs in range(iNum_objs):

            obj_pos_x = random.randint(10, W - 10)
            obj_pos_y = random.randint(10, H - 10)
            obj_size_x = random.randrange(5,25,5)
            obj_size_y = obj_size_x

            tObjects = pygame.Rect(obj_pos_x,obj_pos_y,obj_size_x,obj_size_y)
            self.lScreen_objs.append(tObjects)


    def update(self,index):

        obj_x = (self.lScreen_objs[index][2]) # Get the obj size and shape so not to draw of screen
        obj_y = (self.lScreen_objs[index][3])

        self.lScreen_objs[index][0] = random.randint(obj_x, W - obj_x) # Giving a new position on the index x value
        self.lScreen_objs[index][1] = random.randint(obj_y, W - obj_y) # Giving a new position on the index y value


    def draw_obj(self):

        for num, obj in enumerate(new_goal.lScreen_objs):
            if check_collision(obj):
                new_goal.update(num)
            pygame.draw.rect(screen,get_colours('Red'),(obj))

class Hud(object):
    ''' '''

def get_distance(obj,player):

    ''' Get distance between objects '''

    dist_matrix = []

    for x in obj:
        dis_x = x[0] - player[0]
        dis_y = x[1] - player[1]
        dist_matrix.append(int(math.sqrt((dis_x) **2 + (dis_y **2))))

    return(dist_matrix.index(min(dist_matrix)),min(dist_matrix))

def check_collision(obj):

    if obj.colliderect(new_player.tPlayer_obj):
        return(True)

def Hud():
    ''' '''

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((H,W))
screen_center = (H/2,W/2)
font1 = pygame.font.Font(None,24)
pygame.mouse.set_visible(True)
framerate = pygame.time.Clock()

count = 0
score = 0

#all_sprites = pygame.sprite.Group()
new_player = Player()
new_goal = Goal()

#all_sprites.add(player)
#all_sprites.add(new_goal)

# Start the main game loop
while True:
    # Adding framerate to Window title bar
    pygame.display.set_caption(TITLE + " - %d Fps" % framerate.get_fps())
    # Set the frame rate
    framerate.tick(FPS)
    # Grab the game ticks then convert from milliseconds to seconds
    seconds = pygame.time.get_ticks() / 1000
    # Fill the screen black to wipe before we update
    screen.fill(get_colours('Black'))


    keys = pygame.key.get_pressed()
    new_player.update_player(keys)
    new_player.draw_player()
    new_goal.draw_obj()

    dis_check = get_distance(new_goal.lScreen_objs,new_player.tPlayer_obj)

    timer = print_text(font1,9,560, 'Timer: ' + str(seconds))
    screen.blit(timer[0],timer[1])

    play_score = print_text(font1,10,540,'Score: ' + str(score))
    screen.blit(play_score[0],play_score[1])

    new_dis = print_text(font1,10,580,'Distance: ' + str(dis_check[1]))
    screen.blit(new_dis[0],new_dis[1])

    close_x = (new_goal.lScreen_objs[dis_check[0]][0] + (new_goal.lScreen_objs[dis_check[0]][2]) /2)
    close_y = (new_goal.lScreen_objs[dis_check[0]][1] + (new_goal.lScreen_objs[dis_check[0]][3]) /2)

    pygame.draw.aaline(screen,get_colours('White'),(close_x,close_y),(new_player.tPlayer_obj[0] + new_player.tPlayer_cen[0], new_player.tPlayer_obj[1] + new_player.tPlayer_cen[1]),10)

    for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            elif event.type == KEYUP:
                key_flag = True

            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()

    pygame.display.update()
