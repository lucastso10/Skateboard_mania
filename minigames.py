import pygame

class QuadradoComBola:
    def __init__(self, minigame, modificador, x, y, size):
        self.arena = pygame.Rect(x, y, size, size)
        self.minigame = minigame        #minigame atual
        self.modificador = modificador  #mod de dificuldade
        self.tamanhoPlayer = size // 10
        self.player = pygame.Rect(self.arena.centerx - self.tamanhoPlayer // 2, self.arena.centery - self.tamanhoPlayer // 2, self.tamanhoPlayer, self.tamanhoPlayer)
        self.velocidadeBola = 5

    def draw(self, surface):
        pygame.draw.rect(surface, (128,128,128), self.arena) # desenha arena
        pygame.draw.rect(surface, (0,0,255), self.player) # desenha player
        

    def update(self, surface):
        #atualizar modificador
        pass
        

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
            vel_y -= self.velocidadeBola
        if keys[pygame.K_s]: 
            vel_y += self.velocidadeBola
        if keys[pygame.K_a]:  
            vel_x -= self.velocidadeBola
        if keys[pygame.K_d]:  
            vel_x += self.velocidadeBola
        
        self.moverPlayer(vel_x,vel_y)