import pygame
import random

class Obstaculo:
    def __init__(self):
        self.rects = []
        self.timer = 0
        self.frequencia = 2000
        self.ultimoRect = pygame.time.get_ticks()
        self.lifespan = 3000
    
    def spawn(self, arena):
        #limites da arena
        x_min, y_min = arena.arena.x, arena.arena.y
        x_max, y_max = arena.arena.x + arena.arena.size[0], arena.arena.y + arena.arena.size[1]

        # Tamanho do retângulo
        rect_width = 10
        rect_height = arena.arena.size[1]

        # Posição aleatória dentro da arena
        rect_x = random.randint(x_min, x_max - rect_width)
        rect_y = random.randint(y_min, y_max - rect_height)

        # Escolher o lado correto (acima ou abaixo do retângulo)
        side = random.choice(["Esquerda", "Direita"])
        self.rects.append((pygame.Rect(rect_x, rect_y, rect_width, rect_height), side))


    def update(self, arena):
        # Adiciona novos retângulos periodicamente
        now = pygame.time.get_ticks()
        if now - self.ultimoRect > self.frequencia:
            self.spawn(arena)
            self.ultimoRect = now

        

    def draw(self, surface):
        for rect, side in self.rects:
            color = (0,255,0) if side == "Direita" else (255,0,0)
            pygame.draw.rect(surface, color, rect)

    def check_collision(self, ball_x, ball_y):
        for rect, side in self.rects:
            if side == "left" and ball_x < rect.right:
                return False  # A bola está no lado errado
            elif side == "right" and ball_x > rect.left:
                return False  # A bola está no lado errado
        return True
    
    def draw_time_bar(self, surface, start_ticks, total_time, x, y, width, height ):
    # Calcular o tempo restante
        elapsed_time = pygame.time.get_ticks() - start_ticks
        remaining_time = max(0, total_time - elapsed_time)  # Garantir que o tempo não fique negativo
        progress = remaining_time / total_time  # Proporção de tempo restante

        # Calcular a largura da barra de tempo
        bar_width = width * progress

        # Desenhar a barra de tempo
        pygame.draw.rect(surface, (0,0,0), (x, y, width, height))  # Fundo da barra (preta)
        pygame.draw.rect(surface, (0,0,255), (x, y, bar_width, height))  # Barra de progresso