import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


import pygame
pygame.init()

from Code.bloc import Block
from Code.Constants.Colors import *
from Code.Constants.Dimensions import *




class Snake:

    def __init__(self,WINDOW) :
        self.WINDOW = WINDOW
        
        self.body = []

        self.head = Block(self.WINDOW,0,0,'right', RED)
        self.body.append(self.head)
        self.queue = self.head

        self.direction = self.head.direction
        self.corners = {} #key : (i,j) #value : 'right', 'left', 'up', 'down' --> stores the points where the snake changes its direction


        
    def add_block(self):
        if self.queue.direction == 'right':
            self.queue = Block(self.WINDOW,self.queue.coordinates[0]-1,self.queue.coordinates[1],self.queue.direction)
        elif self.queue.direction == 'left':
            self.queue = Block(self.WINDOW,self.queue.coordinates[0]+1,self.queue.coordinates[1],self.queue.direction)
        elif self.queue.direction == 'up':
            self.queue = Block(self.WINDOW,self.queue.coordinates[0],self.queue.coordinates[1]+1,self.queue.direction)
        else:
            self.queue = Block(self.WINDOW,self.queue.coordinates[0],self.queue.coordinates[1]-1,self.queue.direction)
        self.body.append(self.queue)

        
    
    def add_corner(self,coordinates,new_direction):
        opposite_direction = {
            'right' : 'left',
            'left' : 'right',
            'up' : 'down',
            'down' : 'up'
        }
        if self.direction != opposite_direction[new_direction]:
            self.corners[coordinates] = new_direction
    
    def remove_corner(self,coordinates):
        del self.corners[coordinates]
    
    def move(self):
        for bloc in self.body:
            bloc.move()
            if bloc.coordinates in self.corners:
                bloc.update_direction(self.corners[bloc.coordinates])
                if bloc == self.queue:
                    self.remove_corner(bloc.coordinates)
    

    def draw(self):
        for block in self.body:
            block.draw()
