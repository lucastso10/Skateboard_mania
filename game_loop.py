import pygame
from pygame.locals import *
from menu import Menu, MenuType
from game import Game, Difficulty, Minigames
from minigames import QuadradoComBola
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
        self.minigame = Minigames.DODGE
        self.difficulty = Difficulty.EASY

        self.game = Game()
        self.menu = Menu()
        self.jogador = QuadradoComBola(self.minigame, self.difficulty, 
                                         (self.screen_width // 2) - (self.size // 2),   #posição x
                                         (self.screen_height // 2) - (self.size // 2),  #posição y
                                         self.size) #tamanho quadrado
        
        self.obstaculos = Obstaculo()
        self.clock = pygame.time.Clock()

    def run(self):
        start_ticks = pygame.time.get_ticks()
        total_time = 10000
        while self.running:
            # lidar com eventos pygame aqui
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

                    
            
            keys = pygame.key.get_pressed()
            QuadradoComBola.inputHandle(self.jogador,keys)

            self.obstaculos.update(self.jogador)
            
            self.screen.fill((0,0,0))
            QuadradoComBola.draw(self.jogador, self.screen)
            self.obstaculos.draw(self.screen)
            #QuadradoComBola.update(self.jogador, self.screen)

            # if self.menu_type != MenuType.NONE:
            #     self.menu.update(self, self.menu_type)
            # else:
            #     self.game.update(self)

            self.obstaculos.draw_time_bar(self.screen, start_ticks, total_time, 50, 20, self.size, 10)

            print(self.obstaculos.check_collision())

            pygame.display.flip()
            self.clock.tick(60)
