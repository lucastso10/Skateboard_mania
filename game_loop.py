import pygame
import random
from pygame.locals import *
from menu import Menu, MenuType
from minigames import Minigame, MinigameState, Difficulty, MinigameTypes, Modificadores
from obstaculo import Obstaculo


class GameLoop:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.size = 300     #tamanho quadrado

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Skate Board Mania!")

        self.running = True

        self.menu_type = MenuType.START
        self.difficulty = Difficulty.EASY
        self.pick_minigame()

        self.menu = Menu()
        self.lifes = 3
        self.minigame = Minigame(self)
        
        self.clock = pygame.time.Clock()


    def run(self):
        start_ticks = pygame.time.get_ticks()
        total_time = 10000
        while self.running:
            # lidar com eventos pygame aqui
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.screen.fill((0,0,0))

            keys = pygame.key.get_pressed()
            self.minigame.run(self.screen, keys)

            if self.minigame.state != MinigameState.RUNNING:
                if self.minigame.state == MinigameState.LOST:
                    self.lifes -= 1
                self.pick_minigame()
                self.minigame = Minigame(self)

            pygame.display.flip()
            self.clock.tick(60)

    def pick_minigame(self):
        self.currentModificador = random.choice(Modificadores.all())
        self.currentMinigame = random.choice(MinigameTypes.all())
