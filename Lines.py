'''
Created on 16 Oct 2012

@author: jcrowe
'''

import sys, pygame

#user_w = int(input())
#user_h = int(input())

# creating a tuple to pass later as a colour
COLOR_BLUE,COLOR_BLACK,COLOR_RED,COLOR_GREEN,COLOR_WHITE = (0,0,255),(0,0,0),(255,0,0),(170,255,170),(255,255,255)
S_WIDTH,S_HEIGHT = 500, 500

TOP_CENTER = S_WIDTH/2, S_HEIGHT - S_HEIGHT + 1
BOTTOM_CENTER = S_WIDTH/2, S_HEIGHT - 1
SIDE_CENTER_LEFT = S_WIDTH - S_WIDTH + 1,S_HEIGHT/2
SIDE_CENTER_RIGHT = S_WIDTH -1, S_HEIGHT /2

S_TOP_LEFT = S_WIDTH - S_WIDTH +1, S_HEIGHT - S_HEIGHT +1
S_BOTTOM_LEFT = S_WIDTH - S_WIDTH +1,S_HEIGHT -1
S_TOP_RIGHT = S_WIDTH -1 , 0
S_BOTTOM_RIGHT = S_WIDTH -1, S_HEIGHT -1

screen_base = pygame.display.set_mode((S_WIDTH,S_HEIGHT)) # setting the size of the base surface
running = 1 # Variable to keep the  loop running and to give us a simple quite function 

while running: # check that loop is running
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0 
    
    screen_base.fill(COLOR_BLACK) #filling screen will black
    
    size = int(S_WIDTH/2) # screen / 2
    step = 10 # counts in multiples. 25 lines 10/250
    color = 255,255,255 #colour
           
    
    for x in range(0,size,step):
    # Start at 0, max is Size
    # 0 on the x - we don't want this to move, then we take away the step from size
    # x then jumps buy 5 which is the step, the y we don't want to move
    
    # From 0 to size -x which is the step 5 
        
        pygame.draw.line(screen_base,COLOR_GREEN,(0,size -x),(x,0))
        pygame.draw.line(screen_base,COLOR_WHITE,(S_WIDTH -(size-x),0),(S_WIDTH,x))
        pygame.draw.line(screen_base,COLOR_RED,(0,S_HEIGHT - x),(size -x,S_WIDTH))
        pygame.draw.line(screen_base,COLOR_BLUE,(S_WIDTH,S_HEIGHT-x),(size + x,S_HEIGHT))
        

    pygame.display.flip()
        
        
        
        

    