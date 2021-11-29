import pygame



pygame.init()


BLACK = (0,0,0)
WHITE = (255,255,255)
GRIS = (50,50,50)
RED = (175,0,0)


BLOCK_SIDE = 16

WINDOW_WIDTH, WINDOW_HEIGHT = BLOCK_SIDE*50,BLOCK_SIDE*40


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game v1")


def draw_window():
    WINDOW.fill(BLACK)
    for i in range(50):
        pygame.draw.line(WINDOW,GRIS,(i*BLOCK_SIDE - 1,0),(i*BLOCK_SIDE - 1,WINDOW_HEIGHT),2)
        pygame.draw.line(WINDOW,GRIS,(0,i*BLOCK_SIDE-1),(WINDOW_WIDTH,i*BLOCK_SIDE-1),2)
    pygame.draw.rect(WINDOW,RED,pygame.Rect(10*BLOCK_SIDE,10*BLOCK_SIDE,BLOCK_SIDE,BLOCK_SIDE))
    pygame.display.update()


def main():
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
        draw_window()
    pygame.quit()



if __name__ == '__main__':
    main()