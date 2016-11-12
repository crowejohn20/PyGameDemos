'''
Created on 22 Nov 2012

@author: jcrowe
'''
'''
Created on 29 Oct 2012
@author: jcrowe
'''

# Move a single pixel around the screen without crashing against the borders.

import sys, random, time, pygame
from pygame.locals import *

class Worm:
    
    ''' The worm class is the blueprint of the worm and describes how what parts are involved in building it. Creating lots of worms
        from this class would be called an instance of the class. Class = worm. Worm1, Worm2, Worm3 might be instances of it. '''
    
    def __init__(self, surface, x,y, body_length): # init method
        
        ''' 
            __init__ - This is the initialiser for the class. It gets passed
                       whatever was called with.
                       
                       This method is roughly what represents a CONSTRUCTOR in Python.
                       When we call Worm() Python creates an object for you, and passes it as
                       the first parameter to the __init__ method. Any additional parameters (e.g, Surface,
                       x,y) will also get passed as arguments. 
            
            Example: - If we called x = Worm(10,'foo'), __init__ would get passed 10 and 'foo'
                       as arguments.  x = Worm(Self (OBJECT),10,foo). __init__ is almost universally 
                       used in Python class definitions. 
            
            Why:     - Initialising the worm using values passed into it. 
                     - Giving the worm a surface to be drawn on.
                     - Position of the worm x,y
                     - The length of the worms body 
        '''
        
        self.surface = surface            # Surface to draw on
        self.x = surface.get_width() /2   # x variable
        self.y = surface.get_height() /2  # y variable
        self.length = 1                   # Length of body
        self.grow_to = 50
        self.vx = 0                       # Direction of x
        self.vy = -1                      # Direction of y
        self.body = []                    # This is the list of the positions on each pixel making up the snakes body
        self.colour = (255,255,255)      # Number of  colours
        self.crashed = False              # Bool to check if it's crashed over the edge of screen
        
    
    def eat(self):
        self.grow_to += 25
        
    def event(self, event):
        ''' Handle keyboard events that affect the worm '''
        
        if event.key == pygame.K_UP:
            self.vx = 0
            self.vy = -1
        
        elif event.key == pygame.K_DOWN:
            self.vx = 0
            self.vy = 1
        
        elif event.key == pygame.K_LEFT:
            self.vx = -1
            self.vy = 0
            
        elif event.key == pygame.K_RIGHT:
            self.vx = 1
            self.vy = 0
        
        elif event.key == pygame.K_RETURN:
            pygame.time.wait(10000)
        else:
            return
    
    def move(self):
        ''' function to move the worm '''
        
        self.x += self.vx # Updating the direction of the x 
        self.y += self.vy # Updating the direction of the y
        
        if (self.x, self.y) in self.body:
            self.crashed = True
        
        self.body.insert(0,(self.x,self.y)) #Inserts a new body part pixel to the top of the list
        
        if (self.grow_to > self.length):
            self.length +=1
                
        if len(self.body) > self.length:
            self.body.pop()
    
        
    def draw(self):    
        for x,y in self.body:
            pygame.draw.rect(self.surface, (255,255,255),(int(x),int(y),5,5))
            #self.surface.set_at((int(x),int(y)), self.colour)
    
    def position(self):
        return (int(self.x),int(self.y))

class Food():
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(0, surface.get_width() - 10)
        self.y = random.randint(0, surface.get_height() - 10)
        self.color = (255,255,255)
    
    def draw(self):
        pygame.draw.rect(self.surface,(255,255,255),(self.x,self.y,5,5))
        #self.surface.set_at((self.x,self.y),self.color)
    
    def position(self):
        return (int(self.x),int(self.y))
    
    def check(self, x, y):
        if x < self.x or x > self.x + 3:
            return False
        elif y < self.y or y > self.y + 3:
            return False
        else:
            return True
        
        
def print_text(font,x,y,text,colour =(255,255,255)):
    imgText = font.render(text, True, colour)
    screen.blit(imgText,(x,y))
            
# Dimensions
pygame.init()
w = 240   # Width
h = 180   # Height
body_length = 50
obj_size = 100
score = 0
base_fill = (0,0,0)

pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((w,h))
font1 = pygame.font.Font(None,24)
clock = pygame.time.Clock()

running = True

# Our main Worm
worm_main = Worm(screen, w/2,h/2,body_length)
food = Food(screen)

while running:
    
    screen.fill((0,0,0))
    worm_main.draw()
    worm_main.move()
    food.draw()
    
    print_text(font1,10,10,'Score  ' + str(score))
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
        if event.type == pygame.KEYDOWN:
            worm_main.event(event)
            
        
    if worm_main.crashed or worm_main.x <= 0 or worm_main.x >= w or worm_main.y <= 0 or worm_main.y >= h:
        print('Crash!')
        running = False
    
    if food.check(int(worm_main.x),int(worm_main.y)) == True:
        score +=1
        worm_main.eat()
        print('Score: %d' % score)
        food = Food(screen)
            
    clock.tick(130)
    pygame.display.update()
    
    