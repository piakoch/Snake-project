import pygame
import sys 

def run_game():
    # create the screen (width, height, title, colour etc)
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("ultimate Snake")
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the game state

        pygame.display.update()


run_game()
