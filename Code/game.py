import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

import pygame
from Code.Constants.Colors import *
from Code.Constants.Dimensions import *
from Code.bloc import Block


class Game:
    def __init__(self):

        #Création de la fenêtre 
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game v1")


        #Création d'un bloc 
        self.block = Block(0,0,'right',RED)
    
    def handle_input(self,event):
        key_to_direction = {pygame.K_RIGHT : 'right', pygame.K_LEFT : 'left', pygame.K_UP : 'up', pygame.K_DOWN : 'down'} #d'une clé clavier donne une direction en string
        if event.type == pygame.KEYDOWN:
            if event.key in key_to_direction.keys():
                self.block.update_direction(key_to_direction[event.key])
           
            # if event.key == pygame.K_RIGHT:
            #     self.block.move_right()
            # if event.key == pygame.K_LEFT:
            #     self.block.move_left()
            # if event.key == pygame.K_UP:
            #     self.block.move_up()
            # if event.key == pygame.K_DOWN:
            #     self.block.move_down()
    
    def draw_window(self):

        #on dessine un fond noir sur notre fenêtre
        self.WINDOW.fill(BLACK)

        #on dessine les petites barres permettant de visualiser le découpage de la fenêtre en petits carrés
        for i in range(50):
            pygame.draw.line(self.WINDOW,GRIS,(i*BLOCK_SIDE - 1,0),(i*BLOCK_SIDE - 1,WINDOW_HEIGHT),2)
            pygame.draw.line(self.WINDOW,GRIS,(0,i*BLOCK_SIDE-1),(WINDOW_WIDTH,i*BLOCK_SIDE-1),2)

        #dessin du bloc     
        pygame.draw.rect(self.WINDOW,self.block.color, self.block.rect)
        
        #mise à jour de la fenêtre dès qu'on a tout dessiné
        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():

                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                self.handle_input(event)


            self.block.move()
            self.draw_window()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
