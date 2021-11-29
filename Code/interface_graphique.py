import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


import pygame
from bloc import Block
from Constants.Colors import *

pygame.init()



BLOCK_SIDE = 16

WINDOW_WIDTH, WINDOW_HEIGHT = BLOCK_SIDE*50,BLOCK_SIDE*40


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game v1")


def draw_window(block):
    WINDOW.fill(BLACK)
    for i in range(50):
        pygame.draw.line(WINDOW,GRIS,(i*BLOCK_SIDE - 1,0),(i*BLOCK_SIDE - 1,WINDOW_HEIGHT),2)
        pygame.draw.line(WINDOW,GRIS,(0,i*BLOCK_SIDE-1),(WINDOW_WIDTH,i*BLOCK_SIDE-1),2)
    #pygame.draw.rect(WINDOW,RED,pygame.Rect(10*BLOCK_SIDE,10*BLOCK_SIDE,BLOCK_SIDE,BLOCK_SIDE))
    pygame.draw.rect(WINDOW,block.color, block.rect)
    pygame.display.update()


def main():
    running = True
    block = Block(0,0,RED)
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    block.move_right()
                if event.key == pygame.K_LEFT:
                    block.move_left()
                if event.key == pygame.K_UP:
                    block.move_up()
                if event.key == pygame.K_DOWN:
                    block.move_down()


        draw_window(block)
    pygame.quit()



if __name__ == '__main__':
    main()