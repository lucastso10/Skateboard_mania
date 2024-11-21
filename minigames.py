import pygame.gfxdraw       #deixa a bola lisa :)

class QuadradoComBola:
    def __init__(self, minigame, modificador, x, y, size):
        self. x = x     #pos quadrado
        self. y = y     #pos quadrado
        self.size = size        #tamanho quadrado
        self.minigame = minigame        #minigame atual
        self.modificador = modificador  #mod de dificuldade
        self.tamanhoBola = size // 12   
        self.centroBola = [self.x + self.size // 2, self.y + self.size // 2]    #pos para começar no meio do quadrado
        self.velocidadeBola = 5 * self.modificador      

    def draw(self, surface):
        pygame.draw.rect(surface, (128,128,128), (self.x, self.y, self.size, self.size))        #desenha quadrado

        #centroQuadradoX = self.x + self.size // 2
        #centroQuadradoY = self.y + self.size // 2

        pygame.gfxdraw.aacircle(surface, round(self.centroBola[0]), round(self.centroBola[1]), self.tamanhoBola, (0, 0, 255))  # Contorno
        pygame.gfxdraw.filled_circle(surface, round(self.centroBola[0]), round(self.centroBola[1]), self.tamanhoBola, (0, 0, 255))  # Interior
        

    def update(self, surface):
        #atualizar modificador
        pass
        

    def moverBola(self, vel_x, vel_y):
        self.centroBola[0] += vel_x         
        self.centroBola[1] += vel_y         

        self.centroBola[0] = max(self.x + self.tamanhoBola, min(self.x + self.size - self.tamanhoBola, self.centroBola[0])) 
        self.centroBola[1] = max(self.y + self.tamanhoBola, min(self.y + self.size - self.tamanhoBola, self.centroBola[1]))

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
        
        self.moverBola(vel_x,vel_y)