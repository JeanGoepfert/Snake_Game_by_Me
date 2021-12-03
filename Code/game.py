import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


import pygame
pygame.init()

import random

from Code.Constants.Colors import *
from Code.Constants.Dimensions import *

from Code.snake import Snake
from Code.apple import Apple


class Game:
    def __init__(self):

        #Création de la fenêtre 
        self.WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game v1")

        self.mouvement_allowed = True


        #création d'un serpent
        self.snake = Snake(self.WINDOW)

        #générer une pomme
        self.apple = self.new_apple()
        #booléen qui gère la fin de partie
        self.end = False
        
        self.score = 0

    
    def handle_input(self,event):
        key_to_direction = {    #d'une clé clavier donne une direction en string
            pygame.K_RIGHT : 'right', 
            pygame.K_LEFT : 'left', 
            pygame.K_UP : 'up', 
            pygame.K_DOWN : 'down'
            } 
        if event.type == pygame.KEYDOWN:
            if event.key in key_to_direction.keys() and self.mouvement_allowed:
                new_direction = key_to_direction[event.key]
                self.snake.head.update_direction(new_direction)
                self.snake.direction = new_direction
                self.snake.add_corner((self.snake.head.coordinates),new_direction)
                self.mouvement_allowed = False
            if event.key == pygame.K_SPACE:
                self.snake.add_body_block()
            
            if event.key == pygame.K_p:
                game.pause(10000)

           
    def pause(self,time):
        pygame.time.delay(time)
    
    def end_game(self):

        self.pause(5000)
    

    def new_apple(self):
        snake_positions = [body_block.coordinates for body_block in self.snake.body]
        available_positions = [(i,j) for i in range(50) for j in range(40) if (i,j) not in snake_positions]

        i,j = random.choice(available_positions)
        return Apple(self.WINDOW,i,j)
            
    def draw_window(self):

        #on dessine un fond noir sur notre fenêtre
        self.WINDOW.fill(BLACK)

        #on dessine les petites barres permettant de visualiser le découpage de la fenêtre en petits carrés
        for i in range(50):
            pygame.draw.line(self.WINDOW,GRIS,(i*BLOCK_SIDE - 1,0),(i*BLOCK_SIDE - 1,WINDOW_HEIGHT),2)
            pygame.draw.line(self.WINDOW,GRIS,(0,i*BLOCK_SIDE-1),(WINDOW_WIDTH,i*BLOCK_SIDE-1),2)


        #dessin de la pomme
        self.apple.draw()

        #dessin du serpent
        self.snake.draw()
        
        #mise à jour de la fenêtre dès qu'on a tout dessiné
        pygame.display.update()



    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(FPS)
            self.mouvement_allowed = True

            

            for event in pygame.event.get():

                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                self.handle_input(event)
            
            self.snake.move()

            self.end = self.snake.check_collision()
            if self.end:
                self.snake.move_back()
            
            if self.snake.eat_apple(self.apple):
                self.apple = self.new_apple()

            self.draw_window()

            
            
        pygame.quit()
        

if __name__ == "__main__":
    game = Game()
    game.run()
