import json
import threading

import websocket

import net.client
from ui import ui_manager


class GameController:
    TOKEN = ''

    def __init__(self):
        pass

    def update_player_info(self, data):
        ui_manager.update_player_info(data)

    def update_table_info(self, data):
        ui_manager.update_table_info(data)

    def start_game(self):
        ui_manager.init_main_window()
        username = ui_manager.load_login_ui()

        # do login
        def run_login():
            ws = net.client.create_instant_ws_client('ws://localhost:8080/login', [])
            ws.send(json.dumps(
                {
                    'username': username
                }
            ))
            result_data = ws.recv()
            result = json.loads(result_data)
            self.TOKEN = result['token']
            ws.close(timeout=1)
        login_thread = threading.Thread(target=run_login)
        login_thread.start()
        login_thread.join()

        ui_manager.load_matching_table_ui()
        ui_manager.unload_matching_table_ui()

        token_header = "Game-Token: " + self.TOKEN
        net.client.create_long_lived_ws_client('ws://localhost:8080/game', [token_header])

        ui_manager.init_ui()
        ui_manager.init_user_window()  # we block here

