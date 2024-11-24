import pygame
from obstaculo import Obstaculo
from macros import RectType, MinigameState, MinigameTypes, Modificadores

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

        self.obstaculo = Obstaculo(game.currentMinigame, self.arena)

        self.ended = False

        self.state = MinigameState.RUNNING

        self.start = pygame.time.get_ticks()

        self.animationDuration = 2000
        self.isInAnimation = True

        if self.modificador == Modificadores.RAPIDO:
            self.duration = 2000 // ((((game.minigameCount / 100) * game.difficulty) + 1) * 2)
        else:
            self.duration = 2000 // (((game.minigameCount / 100) * game.difficulty) + 1)

        self.fonte = pygame.font.SysFont("Arial", 20)

    def draw(self, surface):
        pygame.draw.rect(surface, (128,128,128), self.arena) # desenha arena
        pygame.draw.rect(surface, (0,0,255), self.player) # desenha player

    def drawAnimation(self, surface):
        if self.get_elapsed_time() <= self.animationDuration // 2:
            texto = self.fonte.render("Minigame:", True, (255, 255, 255))
            surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery - 25))
            match self.currentMinigame:
                case MinigameTypes.MOVER_CIMA:
                    texto = self.fonte.render("Mova para cima!", True, (255, 255, 255))
                    surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery))
                case MinigameTypes.MOVER_BAIXO:
                    texto = self.fonte.render("Mova para baixo!", True, (255, 255, 255))
                    surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery))
                case MinigameTypes.MOVER_DIREITA:
                    texto = self.fonte.render("Mova para direita!", True, (255, 255, 255))
                    surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery))
                case MinigameTypes.MOVER_ESQUERDA:
                    texto = self.fonte.render("Mova para esquedar!", True, (255, 255, 255))
                    surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery))
                case MinigameTypes.EQUILIBRAR:
                    texto = self.fonte.render("Se equilibre!", True, (255, 255, 255))
                    surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery))

        elif self.get_elapsed_time() <= self.animationDuration:
            texto = self.fonte.render("Modificador:", True, (255, 255, 255))
            surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery - 25))
            match self.modificador:
                case Modificadores.RAPIDO:
                    texto = self.fonte.render("Rápido!", True, (255, 255, 255))
                    surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery))
                case Modificadores.DEVAGAR:
                    texto = self.fonte.render("Devagar!", True, (255, 255, 255))
                    surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery))
                case Modificadores.NEGATIVO:
                    texto = self.fonte.render("Ao contrário!", True, (255, 255, 255))
                    surface.blit(texto, (self.arena.centerx - texto.get_size()[0] // 2, self.arena.centery))
        else:
            self.isInAnimation = False
            self.start = pygame.time.get_ticks()


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
        if self.isInAnimation:
            self.drawAnimation(screen)
        else:
            self.draw_time_bar(screen)
            self.inputHandle(keys)

            self.draw(screen)
            self.obstaculo.draw(screen, self)

            self.win_condition()

    def get_elapsed_time(self):
            return pygame.time.get_ticks() - self.start

    def win_condition(self):
        colisao = self.obstaculo.check_collision(self.player)
        if colisao:
            if colisao == RectType.RED:
                if not self.modificador == Modificadores.NEGATIVO:
                    self.state = MinigameState.LOST
                else:
                    self.state = MinigameState.WON
            elif colisao == RectType.GREEN:
                if not self.modificador == Modificadores.NEGATIVO:
                    if self.modificador == Modificadores.DEVAGAR:
                        if self.get_elapsed_time() >= self.duration // 2:
                            self.state = MinigameState.WON
                        else:
                            self.state = MinigameState.LOST
                    else:
                        self.state = MinigameState.WON
                else:
                    self.state = MinigameState.LOST


        if self.get_elapsed_time() >= self.duration:
            if self.currentMinigame == MinigameTypes.EQUILIBRAR:
                self.state = MinigameState.WON
            else:
                self.state = MinigameState.LOST

    def draw_time_bar(self, surface):
        width = 300
        height = 10

        x = self.arena.centerx - width // 2
        y = 50

        texto = self.fonte.render("Tempo restante!", True, (255, 255, 255))

        width_texto, height_texto = texto.get_size()

        surface.blit(
            texto, 
            (
            self.arena.centerx - (width_texto // 2),
            10
            )
        )

        # Calcular o tempo restante
        remaining_time = max(0, self.duration - self.get_elapsed_time())
        progress = remaining_time / self.duration # Proporção de tempo restante

        # Calcular a largura da barra de tempo
        bar_width = width * progress

        # Desenhar a barra de tempo
        pygame.draw.rect(surface, (0,0,0), (x, y, width, height))  # Fundo da barra (preta)
        pygame.draw.rect(surface, (0,0,255), (x, y, bar_width, height))  # Barra de progresso
        if self.modificador == Modificadores.DEVAGAR:
            pygame.draw.rect(surface, (255,0,0), (x + (width // 2) - 1 , y, 2, 10))


