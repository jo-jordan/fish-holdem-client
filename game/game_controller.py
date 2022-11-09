import ui.ui_manager


class GameController:

    def __init__(self):
        pass

    def update_player_info(self, data):
        ui.ui_manager.update_player_info(data)

    def update_game_info(self, data):
        ui.ui_manager.update_game_info(data)
