import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import pygame

from snake import Snake
WIND = pygame.display.set_mode((500,500))

snake = Snake(WIND)

