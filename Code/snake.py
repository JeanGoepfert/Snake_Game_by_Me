import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


import pygame
pygame.init()

from Code.BodyBlock import BodyBlock
from Code.Constants.Colors import *
from Code.Constants.Dimensions import *




class Snake:

    def __init__(self,SURFACE) :
        self.SURFACE = SURFACE
        
        self.body = []

        self.head = BodyBlock(self.SURFACE,0,0,'right', RED)
        self.body.append(self.head)
        self.queue = self.head

        for _ in range(4):
            self.add_body_block()
        


        self.direction = self.head.direction
        self.corners = {} #key : (i,j) #value : 'right', 'left', 'up', 'down' --> stores the points where the snake changes its direction

        

        
    def add_body_block(self):
        if self.queue.direction == 'right':
            self.queue = BodyBlock(self.SURFACE,self.queue.coordinates[0]-1,self.queue.coordinates[1],self.queue.direction)
        elif self.queue.direction == 'left':
            self.queue = BodyBlock(self.SURFACE,self.queue.coordinates[0]+1,self.queue.coordinates[1],self.queue.direction)
        elif self.queue.direction == 'up':
            self.queue = BodyBlock(self.SURFACE,self.queue.coordinates[0],self.queue.coordinates[1]+1,self.queue.direction)
        else:
            self.queue = BodyBlock(self.SURFACE,self.queue.coordinates[0],self.queue.coordinates[1]-1,self.queue.direction)
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
    
    def check_collision(self):
        #vérification que le serpent reste dans le carré de la fenêtre
        if not self.head.rect.colliderect(self.SURFACE.get_rect()):
            return True

        #vérification que le serpent ne touche pas son corps
        if len(self.head.rect.collidelistall(self.body)) > 1:
            return True
        
        return False
        
    
    def move(self):
        for body_block in self.body:
            body_block.move()
            if body_block.coordinates in self.corners:
                body_block.update_direction(self.corners[body_block.coordinates])
                if body_block == self.queue:
                    self.remove_corner(body_block.coordinates)
        
    def move_back(self):
        for body_block in self.body:
            body_block.move_back()
    
    
    

    def draw(self):
        for body_block in reversed(self.body):
            body_block.draw()


    def eat_apple(self,apple):
        pass