import threading

from game.game_controller import GameController
from infra.dispatcher import Dispatcher
from net.client import NetClient
from ui import ui_manager


# 1. login
# (2. match room)
# 3. join table
# 4. start game
#  4.1. table owner is who created the table
#  4.2. table owner control when game starting
#  4.3. everyone can choose any option of 'fold', 'call', 'raise', 'all-in', 'check'
# 5. end game
# 6. exit table
# (7. exit room)
# 8. exit client

# server
# client:
# |net layer: send and receive package
# |dispatcher: resolve package, route
# |pack_sender layer
# |logic layer

def init_net_client():
    def run():
        NetClient()
    threading.Thread(target=run).start()


def init_dispatcher():
    dispatcher = Dispatcher()  # Singleton

    controller = GameController()
    dispatcher.register_logic('game_info', controller.update_game_info)
    dispatcher.register_logic('player_info', controller.update_player_info)


if __name__ == '__main__':
    init_net_client()
    init_dispatcher()
    ui_manager.init_ui()
