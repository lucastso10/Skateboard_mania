import pygame
from game_loop import GameLoop

def main():
    pygame.init()

    gameloop = GameLoop()

    gameloop.run()

    pygame.quit()

if __name__ == "__main__":
    main()
