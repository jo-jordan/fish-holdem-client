import threading

import websocket

from infra.dispatcher import Dispatcher


class NetClient:
    ws = None
    dispatcher = Dispatcher()  # Singleton

    def __init__(self):
        # websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:8080/echo",
                                         on_open=self.__on_open,
                                         on_message=self.__on_message,
                                         on_error=self.__on_error,
                                         on_close=self.__on_close)

        def timer():
            self.ws.send("w2w2w2w2w22")
        threading.Timer(4, timer).start()
        self.ws.run_forever(reconnect=5)

    def send(self, data):
        self.ws.send(data)

    def __on_message(self, ws, message):
        self.dispatcher.on_receive(message)

    def __on_error(self, ws, error): pass

    def __on_close(self, ws, close_status_code, close_msg): pass

    def __on_open(self, ws): pass
