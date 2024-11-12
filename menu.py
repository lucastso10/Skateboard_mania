
class MenuType:
    NONE = 0
    START = 1
    OPTIONS = 2

class Button:
    PLAY = 0
    OPTIONS = 1
    QUIT = 2

class Menu:
    def __init__(self):
        pass

    def update(self, game_loop, menu_type):
        if menu_type == MenuType.START:
            self.update_start(game_loop)
        elif menu_type == MenuType.OPTIONS:
            #self.update_options(game_loop)
            pass

    def update_start(self, game_loop):
        pass
