import pygame
import random
from macros import RectType, MinigameTypes

class Obstaculo:
    def __init__(self, currentMinigame, arena):
        self.rects = []
        self.currentMinigame = currentMinigame

        self.width = 5
        self.height = arena.height
        self.y = arena.top

        self.spawn(arena)
    
    def spawn(self, arena):
        match self.currentMinigame:

            case MinigameTypes.EQUILIBRAR:
                rect1 = pygame.Rect(arena.centerx - 60, arena.top, 10, arena.height)
                rect2 = pygame.Rect(arena.centerx + 60, arena.top, 10, arena.height)
                self.rects.append((rect1, RectType.RED))
                self.rects.append((rect2, RectType.RED))

            case MinigameTypes.MOVER_DIREITA:
                rect1 = pygame.Rect(arena.centerx - 90, arena.top, 10, arena.height)
                rect2 = pygame.Rect(arena.centerx + 90, arena.top, 10, arena.height)
                self.rects.append((rect1, RectType.RED))
                self.rects.append((rect2, RectType.GREEN))

            case MinigameTypes.MOVER_ESQUERDA:
                rect1 = pygame.Rect(arena.centerx - 90, arena.top, 10, arena.height)
                rect2 = pygame.Rect(arena.centerx + 90, arena.top, 10, arena.height)
                self.rects.append((rect1, RectType.GREEN))
                self.rects.append((rect2, RectType.RED))

            case MinigameTypes.MOVER_CIMA:
                rect1 = pygame.Rect(arena.left, arena.centery - 90, arena.width, 10)
                rect2 = pygame.Rect(arena.left, arena.centery + 90, arena.width, 10)
                self.rects.append((rect1, RectType.GREEN))
                self.rects.append((rect2, RectType.RED))

            case MinigameTypes.MOVER_BAIXO:
                rect1 = pygame.Rect(arena.left, arena.centery - 90, arena.width, 10)
                rect2 = pygame.Rect(arena.left, arena.centery + 90, arena.width, 10)
                self.rects.append((rect1, RectType.RED))
                self.rects.append((rect2, RectType.GREEN))
    def draw(self, surface, arena):
        for rect, rectType in self.rects:
            if rectType == RectType.RED:
                cor = (255, 0, 0)
            elif rectType == RectType.GREEN:
                cor = (0, 255, 0)
            pygame.draw.rect(surface, cor, rect)

    def check_collision(self, player):
        for rect, rectType in self.rects:
            if player.colliderect(rect):
                return rectType
        return None
    
