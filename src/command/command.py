import socket
from dataclasses import dataclass

import dc

from . import config, info, led, motion

__all__ = ["Command"]

TYPE_GETTER = "get"
TYPE_SETTER = "set"
TYPE_EVENT = "event"

GROUP_CONFIG = "config"
GROUP_INFO = "info"
GROUP_LED = "led"
GROUP_MOTION = "motion"


@dataclass
class Command:
    id: int
    group: str
    type: str
    command: str

    def run(self, client: socket.socket, *args) -> dc.Response:
        resp = dc.Response(0, None, None)

        if self.group == GROUP_CONFIG:
            return config.run(self.id, self.type, self.command, *args)

        if self.group == GROUP_INFO:
            ...

        if self.group == GROUP_LED:
            return led.run(self.id, self.type, self.command, *args)

        if self.group == GROUP_MOTION:
            return motion.run(client, self.id, self.type, self.command, *args)

        resp.error = f'Type "{self.group}"not found!'
        return resp
