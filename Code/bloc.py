
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import pygame
pygame.init()
from Code.Constants.Colors import *
from Code.Constants.Dimensions import *




class Block(pygame.sprite.Sprite):
    def __init__(self,i,j, color = WHITE):
        super().__init__()
        self.coordinates = (i,j)
        self.color = color
        self.rect = pygame.Rect(i*BLOCK_SIDE,j*BLOCK_SIDE,BLOCK_SIDE,BLOCK_SIDE)

    
 
    def draw(self,SURFACE):
        pygame.draw.rect(SURFACE,self.color, self.rect)
        border = pygame.Rect(self.rect.x+1,
        self.rect.y+1,
        self.rect.width-2,
        self.rect.height-2
        )
        pygame.draw.rect(SURFACE,BLACK, border,1)

    

