'''
Created on Feb 19, 2013

@author: crowejohn20
'''

class Point(object):
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x
    def setx(self,x):
        self.__x = x
    x = property(getx,setx)
    
    
    def gety(self):
        return self.__y
    def sety(self,y):
        self.__y = y
    y = property(gety,sety)
    
    def __str__(self):
        return'{X:' + '{:.Of}'.format(self.__x) + ',y:' + '{:.Of}'.format(self.__y) +'}'
        