'''
Created on Dec 31, 2012

Driving test quiz game to help me study for my license. 

@author: crowejohn20
'''

import sys,pygame
from pygame.locals import *

class Trivia(object):
    def __init__(self,filename):
        self.data = []
        self.current  = 0
        self.total    = 0
        self.correct  = 0
        self.incorret = 0
        self.score    = 0
        self.wrong    = 0
        self.time     = 10
        self.count    = 0
        self.skipped  = True
        self.scored   = False
        self.failed   = False
        self.colours  = [white,white,white,white]
        
        # Read in trivia data from file
        
        quiz_file = open(filename,'r')
        quiz_questions = quiz_file.readlines()
        quiz_file.close()
        
        # Preparing trivia data
        for text_line in quiz_questions:
            question = text_line.split(';')
            for line in question:
                self.data.append(line.strip())
                self.total += 1
                
            
    def question_menu(self):
        print_text(font1,200,5,'Please pick a category')
        print_text(font2,190,500-20,'Press keys (1-4) to answer', purple)
        
    
    def show_questions(self):
        print_text(font1,200,5,'TEST TITLE')
        print_text(font2,190,500-20,'Press keys (1-4) to answer', purple)
        print_text(font2,530,5,'SCORE', purple)
        print_text(font2,450,5,'TIME', purple)
        print_text(font2,550,25,str(self.score), purple)
        print_text(font2,460,25,str(self.time),purple)
        
        # Get the correct answer out of data first
        self.correct = int(self.data[self.current+5])
        
        # Display question
        question = self.current // 6 + 1
        print_text(font1,5,80, 'QUESTION ' + str(question))
        print_text(font2,20,120, self.data[self.current],yellow)
        
        #Respond to correct answer
        if self.scored:
            self.colours = [white,white,white,white]
            self.colours[self.correct-1] = green
            print_text(font1,230,380, 'CORRECT!', green)
            print_text(font1,230,400,self.data[self.current+6], green)
            print_text(font2,170,420,'Press ENTER for the next question', red)
        
        if self.failed:
            self.colours = [white,white,white,white]
            self.colours[self.correct-1] = green
            print_text(font1,230,380, 'INCORRECT', red)
            print_text(font2,100,415,self.data[self.current+6], green)
            print_text(font2,170,440,'Press ENTER for the next question', red)
            
        
        # Display answers
        print_text(font1,5,170,'ANSWERS')
        print_text(font2,20,210,'1 - ' + self.data[self.current+1],self.colours[0])
        print_text(font2,20,240,'2 - ' + self.data[self.current+2],self.colours[1])
        print_text(font2,20,270,'3 - ' + self.data[self.current+3],self.colours[2])
        print_text(font2,20,300,'4 - ' + self.data[self.current+4],self.colours[3])
        
    
    def handle_time(self):
        ''' '''
        
    
    def handle_input(self,number):
        if not self.scored and not self.failed:
            if number == self.correct:
                self.scored = True
                self.score += 1
            else:
                self.failed = True
                self.incorret +=1
                self.wrong = number
            self.skipped = False
                
    def next_question(self):
        if self.scored or self.failed:
            if self.slipped == True:
                self.scored = False
                self.failed = True
                self.correct = 0
                self.colours = [white,white,white,white]
                self.current += 7
                if self.current >= self.total:
                    self.current = 0
                    self.time = 10

def print_text(font,x,y,text, colour=(255,255,255), shadow = True):
    if shadow:
        imgText = font.render(text, True,(0,0,0))
        screen.blit(imgText,(x-2,y-2))
    imgText = font.render(text,True,colour)
    screen.blit(imgText,(x,y))
    

def draw_images():
    pygame.draw.rect(screen, (255,255,255),(200,160,100,100),3)
    pygame.draw.rect(screen, (255,255,255),(310,270,100,100),3)
    pygame.draw.rect(screen, (255,255,255),(310,160,100,100),3)
    pygame.draw.rect(screen, (255,255,255),(200,270,100,100),3)
    
    
# Main program begins

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Driving Test Quiz')
clock_timer = 10
font1  = pygame.font.Font(None,40)
font2  = pygame.font.Font(None,24)
white  = 255,255,255
cyan   = 0,255,255
yellow = 255,255,0
purple = 255,0,255
green  = 0,255,0
red    = 255,0,0
running = True
count = 0
clock = pygame.time.Clock()

# Load the quiz data file
quiz_class = Trivia('questions.txt')

# Game loop, checking for input
while running:
    
    # Clear the screen
    screen.fill((0,0,200))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_ESCAPE]:
                sys.exit()
            elif event.key == pygame.K_1:
                quiz_class.handle_input(1)
            elif event.key == pygame.K_2:
                quiz_class.handle_input(2)
            elif event.key == pygame.K_3:
                quiz_class.handle_input(3)
            elif event.key == pygame.K_4:
                quiz_class.handle_input(4)
            elif event.key == pygame.K_RETURN:
                quiz_class.next_question()
    
    
    # Display trivia data           
    quiz_class.show_questions()
    draw_images()
    
    clock.tick(60)
    pygame.display.update()
    
                

        
            
            
     
        
        