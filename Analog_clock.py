''' 

Created on Dec 27, 2012

Analog Clock demo - Shows the use of circle, radians and degress 

@author: crowejohn20 '''


import sys, random, math, pygame
from datetime import datetime,date,time

today_now = datetime.today() # Getting todays date and time
hours = today_now.hour % 12

# Main program begins

pygame.init()
screen =  pygame.display.set_mode((600,500))
pygame.display.set_caption('Clock Demo')
screen.fill((0,0,0))

font_1 = pygame.font.Font(None, 24)

pos_x  = 300
pos_y  = 250
radius = 200
angle  = 360

def print_text(font,x,y,text, colour=(255,255,255)):
    imgText = font.render(text,True,colour)
    screen.blit(imgText,(x,y))
    
def wrap_angle(angle):
    return angle % 360

# Repeating loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        sys.exit()
        
        
    pygame.draw.circle(screen,(255,255,255),(pos_x,pos_y), radius,6)
    
    for n in range(1,13):
        angle = math.radians(n *(360/12) -90)
        x = math.cos(angle) * (radius -20) -10
        y = math.sin(angle) * (radius - 20) - 10
        print_text(font_1,pos_x+x, pos_y + y, str(n))
        
    # Draw the hr hand
    hour_angle = wrap_angle(hours * (360/12) - 90)
    hour_angle = math.radians(hour_angle)
    hour_x = math.cos(hour_angle) * (radius - 80)
    hour_y = math.sin(hour_angle) * (radius - 80)
    target = (pos_x+hour_x,pos_y+hour_y)
    pygame.draw.aaline(screen,(255,255,255),(pos_x,pos_y),target,25)
        

    pygame.display.update()




'''    # Increment angle
    angle +=1
    if angle >= 360:
        angle = 0
        r =random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        colour = r,g,b

    # calculate coordinates
    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius

    # Draw one step around the circle
    pos = (int(pos_x + x), int(pos_y + y))
    pygame.draw.circle(screen, colour,pos,5,0) '''
