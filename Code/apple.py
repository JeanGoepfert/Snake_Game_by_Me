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

class Apple(Block):

    def __init__(self, WINDOW, i, j, color=GREEN):
        super().__init__(WINDOW, i, j, color=color)

        
    
