import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import pygame
from Code.Constants.Colors import *
from Code.Constants.Dimensions import *

from Code.bloc import Block



class BodyBlock(Block):
    def __init__(self,i,j,direction, color = WHITE):
        super().__init__(i,j, color)

        self.direction = direction #string 
        self.old_direction = self.direction

    
    def move_right(self) : 
        self.coordinates = (self.coordinates[0] + 1,self.coordinates[1])
        self.rect.x +=BLOCK_SIDE
    def move_left(self) : 
        self.coordinates = (self.coordinates[0] - 1,self.coordinates[1])
        self.rect.x -=BLOCK_SIDE
    def move_down(self) : 
        self.coordinates = (self.coordinates[0] ,self.coordinates[1] + 1)
        self.rect.y +=BLOCK_SIDE
    def move_up(self) : 
        self.coordinates = (self.coordinates[0] ,self.coordinates[1] - 1)
        self.rect.y -=BLOCK_SIDE
    
    def move(self):
        self.old_direction = self.direction

        if self.direction == 'up':
            self.move_up()
        elif self.direction == 'down':
            self.move_down()
        elif self.direction == 'right':
            self.move_right()
        elif self.direction == 'left':
            self.move_left()
        else:
            raise ValueError("The direction wasn't in : up, down, right, left")
        
    def move_back(self):
        self.direction = self.old_direction

        if self.direction == 'down':
            self.move_up()
        elif self.direction == 'up':
            self.move_down()
        elif self.direction == 'left':
            self.move_right()
        elif self.direction == 'right':
            self.move_left()

    
    def update_direction(self, new_direction):
        opposite_direction = {
            'right' : 'left',
            'left' : 'right',
            'up' : 'down',
            'down' : 'up'
        }

        if self.direction != opposite_direction[new_direction]:
            self.direction = new_direction
    