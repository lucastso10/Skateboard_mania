import pygame
import random
from pygame.locals import *
from game_loop import GameLoop
from menu import Menu

class Game:
    # se der tempo implementar sensibilidade
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.size = 300     #tamanho quadrado

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Skateboard Mania!")

        self.menu = Menu(self.screen)
        
    def run(self):
        replay = True
        cond = True
        while replay and cond:
            cond = self.menu.run()
            if cond:
                gameLoop = GameLoop(self.screen)
                replay = gameLoop.run()
