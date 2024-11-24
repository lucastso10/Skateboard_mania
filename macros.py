class MinigameState:
    RUNNING = 0
    LOST = 1
    WON = 2

# o tempo vai ser dividido por esse valor
class Difficulty:
    HARD = 1.2
    MEDIUM = 1.1
    EASY = 1

# Adicionar todos os minigames aqui
class MinigameTypes:
    MOVER_DIREITA = 1
    MOVER_ESQUERDA = 2
    MOVER_CIMA = 3
    MOVER_BAIXO = 4
    EQUILIBRAR = 5

    def all():
        return [MinigameTypes.MOVER_CIMA, MinigameTypes.MOVER_BAIXO, MinigameTypes.MOVER_DIREITA, MinigameTypes.MOVER_ESQUERDA, MinigameTypes.EQUILIBRAR]

class Modificadores:
    RAPIDO = 0
    DEVAGAR = 1
    NEGATIVO = 2

    def all():
        return [Modificadores.RAPIDO, Modificadores.DEVAGAR, Modificadores.NEGATIVO]

class RectType:
    RED = 1
    GREEN = 2

class MenuType:
    NONE = 0
    START = 1
    OPTIONS = 2

class Button:
    PLAY = 0
    OPTIONS = 1
    QUIT = 2
