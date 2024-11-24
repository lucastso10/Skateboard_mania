import pygame
from pygame.locals import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.opcoes = ["Começar", "Sair"]

        self.fonte = pygame.font.SysFont("Arial", 20)

        self.running = True

        self.botao1 = pygame.Rect((self.screen.get_size()[0] // 2) - 100, self.screen.get_size()[1] // 2, 200, 50)

        self.botao2 = pygame.Rect((self.screen.get_size()[0] // 2) - 100, (self.screen.get_size()[1] // 2) + 70, 200, 50)
    def run(self):
        while self.running:
            # lidar com eventos pygame aqui
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    posicao = event.pos
                    if self.botao1.collidepoint(posicao):
                        return True
                    if self.botao2.collidepoint(posicao):
                        return False

            self.screen.fill((0,0,0))

            self.draw()

            pygame.display.flip()

    def draw(self):
        pygame.draw.rect(self.screen, (177,177,177), self.botao1)
        pygame.draw.rect(self.screen, (177,177,177), self.botao2)

        texto = self.fonte.render("Iniciar", True, (255, 255, 255))
        self.screen.blit(texto, (self.botao1.centerx - (texto.get_size()[0] // 2),self.botao1.centery - (texto.get_size()[1] // 2)))

        texto = self.fonte.render("Sair", True, (255, 255, 255))
        self.screen.blit(texto, (self.botao2.centerx - (texto.get_size()[0] // 2),self.botao2.centery - (texto.get_size()[1] // 2)))

        texto = self.fonte.render("Skateboard Mania!", True, (255, 255, 255))
        self.screen.blit(texto, ((self.screen.get_size()[0] // 2) - (texto.get_size()[0] // 2), 100))
        
