'''
Created on 29 Oct 2012
@author: jcrowe
''' 

# Move a single pixel around the screen without crashing against the borders.

import pygame

class Worm:
    ''' Information for the attributes of a worm '''
    
    def __init__(self, surface, x,y, body_length): # init method
        
        ''' 
            __init__ - This is the initialiser for the class. It gets passed
                       whatever the primary constructor was called with.
                       
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
        
        self.surface = surface      # Surface to draw on
        self.x = int(x)             # x variable
        self.y = int(y)             # y variable
        self.length = body_length   # Length of body
        self.dir_x = 0              # Direction of x
        self.dir_y = -1             # Direction of y
        self.body = []              # This is the list of the positions on each pixel making up the snakes body
        self.colour = 255,255,255   # Object colour
        self.crashed = False        # Bool to check if it's crashed over the edge of screen
        
    def key_event(self, event):
        ''' Handle keyboard events that affect the worm '''
        
        if event.key == pygame.K_UP:
            self.dir_x = 0
            self.dir_y = -1
        
        elif event.key == pygame.K_DOWN:
            self.dir_x = 0
            self.dir_y = 1
        
        elif event.key == pygame.K_LEFT:
            self.dir_x = -1
            self.dir_y = 0
            
        elif event.key == pygame.K_RIGHT:
            self.dir_x = 1
            self.dir_y = 0
        
    
    def move(self):
        ''' function to move the worm '''
        
        self.x += self.dir_x # Updating the direction of the x 
        self.y += self.dir_y # Updating the direction of the y
        
        if (self.x,self.y) in self.body: # If x,y in body then end game?
            self.crashed = True
            
        self.body.insert(0,(self.x,self.y))
        
        if len(self.body) > self.length:
            self.body.pop()
        
    
    def draw(self):
        for x,y in self.body:
            pygame.draw.rect(screen, (255,255,255),(x,y,5,5),0)
            self.surface.set_at((x,y),self.colour)
            
# Dimensions
w = 640   # Width
h = 480   # Height

screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
running = True

# Our main Worm
worm_main = Worm(screen, w/2,h/2,50)

while running:
    screen.fill((0,0,0))
    worm_main.move()
    worm_main.draw()
    
    if worm_main.crashed or worm_main.x <= 0 or worm_main.x >= w or worm_main.y <= 0 or worm_main.y >= h:
        print('Crash!')
        running = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            worm_main.key_event(event)
    
    
    pygame.display.flip()
    clock.tick(240)