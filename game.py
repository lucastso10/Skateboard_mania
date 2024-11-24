import pygame
import random
from pygame.locals import *


class Game:
    # se der tempo implementar sensibilidade
    def __init__(self):
        self.minigames = Minigames.all()
        self.difficulty = Difficulty.MEDIUM

        # sempre começar no primeiro minigame
        self.current_minigame = self.minigames[0]

        self.clock = pygame.time.Clock()

        self.game_sprites = pygame.sprite.Group()

        # pode aumentar dps
        self.minigame_time = 10.0

        self.changing_minigame = True

        self.paused = False

        
    def initialize_current_minigame(self):
        # implementar a função config em todos os minigames
        self.current_minigame = self.current_minigame.config(self.minigame_time)

    def update(self):
        if self.changing_minigame:
            self.change_minigame_animation()
            
        # implementar a função update em todos os minigames
        self.current_minigame.update()

        if self.current_minigame.ended():
            self.minigame_time /= self.difficulty
            self.current_minigame = random.choice(self.minigames)
            self.change_minigame_animation()

    def change_minigame_animation(self):
        self.changing_minigame = False
        pass
