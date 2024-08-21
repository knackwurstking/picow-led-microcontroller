import socket
from dataclasses import dataclass

import dc

from . import config, info, led
import config as c


TYPE_GETTER = "get"
TYPE_SETTER = "set"
TYPE_EVENT = "event"

GROUP_CONFIG = "config"
GROUP_INFO = "info"
GROUP_LED = "led"


@dataclass
class Command:
    id: int
    group: str
    type: str
    command: str

    def run(self, client: socket.socket, *args):
        resp = dc.new_response(c.ID_DEFAULT)

        if self.group == GROUP_CONFIG:
            return config.run(self.id, self.type, self.command, *args)

        if self.group == GROUP_INFO:
            return info.run(self.id, self.type, self.command, *args)

        if self.group == GROUP_LED:
            return led.run(self.id, self.type, self.command, *args)

        resp["error"] = f'Type "{self.group}"not found!'
        return resp
