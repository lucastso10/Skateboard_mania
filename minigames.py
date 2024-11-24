import pygame
from obstaculo import Obstaculo, RectType

class MinigameState:
    RUNNING = 0
    LOST = 1
    WON = 2

# o tempo vai ser dividido por esse valor
class Difficulty:
    HARD = 1.6
    MEDIUM = 1.4
    EASY = 1.2

# Adicionar todos os minigames aqui
class MinigameTypes:
    MOVER_DIREITA = 0
    MOVER_ESQUERDA = 0
    MOVER_CIMA = 0
    MOVER_BAIXO = 0
    EQUILIBRAR = 1

    def all():
        return [MinigameTypes.MOVER_CIMA, MinigameTypes.MOVER_BAIXO, MinigameTypes.MOVER_DIREITA, MinigameTypes.MOVER_ESQUERDA, MinigameTypes.EQUILIBRAR]

class Modificadores:
    RAPIDO = 0
    DEVAGAR = 1
    CUIDADOSAMENTE = 2
    NEGATIVO = 3

    def all():
        return [Modificadores.RAPIDO, Modificadores.DEVAGAR, Modificadores.CUIDADOSAMENTE, Modificadores.NEGATIVO]

class Minigame:
    def __init__(self, game):
        self.arena = pygame.Rect(
                (game.screen_width // 2) - (game.size // 2), 
                (game.screen_height // 2) - (game.size // 2), 
                game.size, 
                game.size)
        self.tamanhoPlayer = game.size // 10

        self.player = pygame.Rect(self.arena.centerx - self.tamanhoPlayer // 2,
                                  self.arena.centery - self.tamanhoPlayer // 2,
                                  self.tamanhoPlayer, self.tamanhoPlayer)
        self.velocidadePlayer = 5

        self.currentMinigame = game.currentMinigame
        self.modificador = game.currentModificador

        self.obstaculo = Obstaculo()

        self.ended = False

        self.state = MinigameState.RUNNING

    def draw(self, surface):
        pygame.draw.rect(surface, (128,128,128), self.arena) # desenha arena
        pygame.draw.rect(surface, (0,0,255), self.player) # desenha player

    def moverPlayer(self, vel_x, vel_y):
        if vel_x < 0:
            if not self.player.left <= self.arena.left:
                self.player = self.player.move(vel_x, 0)
        else:
            if not self.player.right >= self.arena.right:
                self.player = self.player.move(vel_x, 0)

        if vel_y < 0:
            if not self.player.top <= self.arena.top:
                self.player = self.player.move(0, vel_y)
        else:
            if not self.player.bottom >= self.arena.bottom:
                self.player = self.player.move(0, vel_y)

    def inputHandle(self, keys):
        vel_x, vel_y = 0, 0

        if keys[pygame.K_w]:
            vel_y -= self.velocidadePlayer
        if keys[pygame.K_s]: 
            vel_y += self.velocidadePlayer
        if keys[pygame.K_a]:  
            vel_x -= self.velocidadePlayer
        if keys[pygame.K_d]:  
            vel_x += self.velocidadePlayer
        
        self.moverPlayer(vel_x,vel_y)

    def run(self, screen, keys):
        self.inputHandle(keys)

        self.obstaculo.update(self)
        self.draw(screen)
        self.obstaculo.draw(screen, self)
        
        colisao = self.obstaculo.check_collision(self.player) 
        if colisao != None:
            self.ended = True
            if colisao == RectType.RED:
                self.state = MinigameState.LOST
            elif colisao == RectType.GREEN:
                self.state = MinigameState.WON


