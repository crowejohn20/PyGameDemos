'''
Created on Sep 28, 2012

@author: JC_Macbook
'''
import os, time
from math import *

'''
Checking for ints and strings to pass to the other functions. I could have used one function here and split them using .isdigit() 

'''
def check_int():
    while True:
        try:
            value = input('----> ')
            value = int(value)
            return(value)
        except ValueError:
            print('I need an integer for calculations. Please enter an integer')

def check_str():
    while True:
        try:
            value = input('----> ')
            value = str(value)
            return(value)
        except ValueError:
            print('I need a string. Please enter an string')
           


'''
Tests for a remainder. Added in some extra validation.

'''

def remainder_test(value):
    print('Hello, Please enter a range of numbers to check for remainders.\n ')
    check_range = check_int()
    
    result = [x for x in range(check_range +1) if x % 2 == 0 ]
    print('Numbers with no remainders in range', check_range, '=' , result)
    return


'''
Working with diagonals at the moment so added this simple test to find the diagonals. Could of handled triangles and lines a little more gracefully but the below code still works fine

'''


def find_diagonals(value):
    print('Hello, Please enter the number of vertices in your polygon.\n')
    num_verts = check_int()
    
    if  num_verts > 3:
        print('You have enough vertices to generate diagonals')
        diag_per_vert = num_verts - 3
        total_diag = diag_per_vert * num_verts / 2 
        print('The number of diagonals are', int(total_diag))
    else:
        print('Your shape does not have enough vertices to generate diagonals')

'''
Fib sequence can't believe i messed this up. Tried to make it as compact and efficient as possible.

'''             

def fib(value):
    
    count = 0
    fib_store = []
    start,tmp = 0,1
    
    print('Hello, Please enter a maximum range of results.\n----> ')
    max_fib = check_int()
    
    for num in range(max_fib):
        fib_store.append(start)
        start,tmp = tmp, start + tmp
         
    for i in fib_store:
        print('Index', count, 'Value',i)
        count += 1
    print('\n Pick a index value to view ')
    index_val = check_int()
    print(fib_store[index_val])


'''
Working with geometry at the moment so added this simple test to find the circles, should really convert it to radians as well since that is the C standard. 

'''
   
def circle():
    
    radious = input('Enter radius')
    diameter = float(radious) * 2
    circum = pi * diameter
    print(circum)
    

'''
Not sure if this is correct, i didnt base it on the command line as I wanted to make the code a little more portable. Could have used the pass by reference class but went for a more simpler menu. 

'''

def docReader():
    
    
    while True:
    
        print('Enter the director to open ')
        direct = check_str()
    
        if os.path.exists(direct):
            break
        else:
            print('That directory does not exist')
    
    print('''\n
    
    Directory lister
    --------------------------------------------------------------

    1. List item in directory
    2. Write contents of directory to file (with execution time)
    3. Run application in directory
    
    ''')
    
    
    dir_menu_choice = check_int()
    
    if dir_menu_choice == 1:
        for items_in_dir in os.listdir(direct):
            print(items_in_dir)
        
    
    if dir_menu_choice == 2:
        print('Enter a file name for content to be stored. ')
        file_name = check_str()
        f = open(direct +'/' + file_name, 'w+')
        exe_time = time.time()
        
        
        print('Writing content to log....')
        
        for items_in_dir in os.listdir(direct):
            items_in_dir = str(items_in_dir)
            f.write(items_in_dir + '\n')
        f.close()
        print (time.time() - exe_time, "seconds")
    
''' Simple menu and validation. Could have used a dictionary to shorted the code but it's not that taxing on resources so what's the point.  '''   

def main():
    while True:
        
        print('''
        
        Math functions 
        --------------------------------------------------------------
        
        1. Remove odd numbers from a list of numbers you specify - ( Question 1 )
        2. Find the number of diagonals within a polygon
        3. Fibonacci sequence indexer - ( Question 2 )
        4. Finding the radius of a circle
        5. Directory reader - ( Question 5b )
        
        --------------------------------------------------------------
        ''')
        
        print('Please enter a choice from 1-5.\n')
        choice = check_int()
        
        if choice == 1:
            remainder_test(choice)
        
        elif choice == 2:
            find_diagonals(choice)
        
        elif choice == 3:
            fib(choice)
        
        elif choice == 4:
            circle()
            
        elif choice == 5:
            docReader()
                      
main()