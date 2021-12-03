
import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import pygame
from Code.Constants.Colors import *
from Code.Constants.Dimensions import *




class Block(pygame.sprite.Sprite):
    def __init__(self,SURFACE,i,j, color = WHITE):
        super().__init__()
        self.coordinates = (i,j)
        self.color = color
        self.rect = pygame.Rect(i*BLOCK_SIDE,j*BLOCK_SIDE,BLOCK_SIDE,BLOCK_SIDE)

        self.SURFACE = SURFACE
    
 
    def draw(self):
        pygame.draw.rect(self.SURFACE,self.color, self.rect)
        border = pygame.Rect(self.rect.x+1,
        self.rect.y+1,
        self.rect.width-2,
        self.rect.height-2
        )
        pygame.draw.rect(self.SURFACE,BLACK, border,1)

    

