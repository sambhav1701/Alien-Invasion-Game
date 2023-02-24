import sys

import pygame

class AlienInvasion:

    def __init__(self):
        self.bg_color = (230, 230, 230)
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        
        
    def run_game(self):
        self.screen.fill(self.bg_color)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

