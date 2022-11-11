import threading

import websocket

from infra.dispatcher import Dispatcher

dispatcher = Dispatcher()


# ws://localhost:8080/login
# ws://localhost:8080/game
def create_instant_ws_client(url, headers):

    ws = websocket.WebSocket()
    ws.connect(url, header=headers)
    return ws


def create_long_lived_ws_client(url, headers):
    def run():

        # websocket.enableTrace(True)
        ws = websocket.WebSocketApp(url,
                                    on_open=__on_open,
                                    on_message=__on_message,
                                    on_error=__on_error,
                                    on_close=__on_close,
                                    header=headers
                                    )
        ws.run_forever(reconnect=5)
    threading.Thread(target=run).start()


def __on_message(ws, message):
    dispatcher.on_receive(message)


def __on_error(ws, error): pass


def __on_close(ws, close_status_code, close_msg): pass


def __on_open(ws):
    ws.send('request start')
