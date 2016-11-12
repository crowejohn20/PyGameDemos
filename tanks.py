'''
Created on Feb 19, 2013

@author: crowejohn20
'''
import math
from tools import *

# calculates velocity of an angle
def angular_velocity(angle):
    vel = Point(0,0)
    vel.x = math.cos(math.radians(angle))
    vel.y = math.sin(math.radians(angle))
    return vel



angle = 5
print(angular_velocity(angle))