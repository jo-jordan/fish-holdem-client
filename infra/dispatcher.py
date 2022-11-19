# on send
# on receive
import json

from infra.singleton import Singleton


def _resolve_pack(data):
    entity = json.loads(data)
    return entity['data_type'], entity


class Dispatcher(metaclass=Singleton):
    logic_dict = {}

    def register_logic(self, name, logic_fun):
        self.logic_dict[name] = logic_fun

    def on_receive(self, data):
        logic, entity = _resolve_pack(data)
        self.logic_dict[logic](entity)

