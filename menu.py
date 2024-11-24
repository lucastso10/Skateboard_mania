
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
