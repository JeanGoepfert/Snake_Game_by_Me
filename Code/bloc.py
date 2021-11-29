import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import pygame
from Constants.Colors import *



BLOCK_SIDE = 16

class Block(pygame.sprite.Sprite):
    def __init__(self,i,j,color):
        super().__init__()
        self.coordinates = [i,j]
        self.color = color
        self.rect = pygame.Rect(i*BLOCK_SIDE,j*BLOCK_SIDE,BLOCK_SIDE,BLOCK_SIDE)
    
    def move_right(self) : 
        self.coordinates[0] += 1
        self.rect.x +=BLOCK_SIDE
    def move_left(self) : 
        self.coordinates[0] -= 1
        self.rect.x -=BLOCK_SIDE
    def move_down(self) : 
        self.coordinates[1] +=1
        self.rect.y +=BLOCK_SIDE
    def move_up(self) : 
        self.coordinates[1] -= 1
        self.rect.y -=BLOCK_SIDE

