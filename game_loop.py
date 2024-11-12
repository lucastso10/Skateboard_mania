import pygame
from pygame.locals import *
from menu import Menu, MenuType
from game import Game

class GameLoop:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Skate Board Mania!")

        self.running = True

        self.menu_type = MenuType.START

        self.game = Game()
        self.menu = Menu()
        
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            # lidar com eventos pygame aqui
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.screen.fill((0,0,0))

            if self.menu_type != MenuType.NONE:
                self.menu.update(self, self.menu_type)
            else:
                self.game.update(self)

            pygame.display.flip()
            self.clock.tick(60)
