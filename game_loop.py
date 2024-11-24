import pygame
import random
from pygame.locals import *
from menu import Menu
from minigames import Minigame
from obstaculo import Obstaculo
from macros import MinigameState, Difficulty, MinigameTypes, Modificadores, MenuType

class GameLoop:
    def __init__(self, screen):
        self.screen_width = 900
        self.screen_height = 600
        self.size = 300     #tamanho quadrado

        self.screen = screen
        self.running = True

        self.difficulty = Difficulty.EASY
        self.lifes = 3
        self.heart = pygame.image.load("imagens/heart.png")
        self.pauseIcon = pygame.image.load("imagens/pause_icon.png")
        self.fonte = pygame.font.SysFont("Arial", 20)

        self.minigameCount = 0
        self.pick_minigame()
        self.pontos = 0

        self.inPause = False

        self.timeOut = 1000
        self.timeOutStart = pygame.time.get_ticks()
        
        self.clock = pygame.time.Clock()

    def run(self):
        start_ticks = pygame.time.get_ticks()
        total_time = 10000
        while self.running:
            # lidar com eventos pygame aqui
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False

            self.screen.fill((0,0,0))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE] and pygame.time.get_ticks() - self.timeOutStart > self.timeOut:
                if self.inPause:
                    self.inPause = False
                else:
                    self.inPause = True
                self.timeOutStart = pygame.time.get_ticks()

            if not self.inPause:
                self.draw_vida()

                self.minigame.run(self.screen, keys)

                if self.minigame.state != MinigameState.RUNNING:
                    if self.minigame.state == MinigameState.LOST:
                        self.lifes -= 1
                    elif self.minigame.state == MinigameState.WON:
                        self.pontos += 100
                    self.pick_minigame()
            else:
                self.draw_pause()

            pygame.display.flip()
            self.clock.tick(60)

            if self.lifes <= 0:
                return True

    def pick_minigame(self):
        self.minigameCount += 1
        self.currentModificador = random.choice(Modificadores.all())
        self.currentMinigame = random.choice(MinigameTypes.all())
        self.minigame = Minigame(self)

    def draw_vida(self):
        texto = self.fonte.render("Vidas:", True, (255, 255, 255))
        self.screen.blit(texto, (self.screen_width - 185, 10))

        offset = 130
        for i in range(self.lifes):
            self.screen.blit(self.heart, (self.screen_width - offset, 0))
            offset -= 35

        texto = self.fonte.render(f"Pontos:{self.pontos}", True, (255, 255, 255))
        self.screen.blit(texto, (10, 10))

    def draw_pause(self):
        self.screen.blit(self.pauseIcon, ((self.screen_width // 2) - (self.pauseIcon.get_size()[0] // 2), (self.screen_height // 2) - (self.pauseIcon.get_size()[1] // 2)))
