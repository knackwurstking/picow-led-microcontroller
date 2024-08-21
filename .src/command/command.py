import dc

import config as c

from . import config, info, led

TYPE_GETTER = "get"
TYPE_SETTER = "set"
TYPE_EVENT = "event"

GROUP_CONFIG = "config"
GROUP_INFO = "info"
GROUP_LED = "led"


class Command:
    def __init__(self, id, group, _type, command):
        self.id = id
        self.group = group
        self.type = _type
        self.command = command

    def run(self, *args):
        resp = dc.new_response(c.ID_DEFAULT)

        if self.group == GROUP_CONFIG:
            return config.run(self.id, self.type, self.command, *args)

        if self.group == GROUP_INFO:
            return info.run(self.id, self.type, self.command, *args)

        if self.group == GROUP_LED:
            return led.run(self.id, self.type, self.command, *args)

        resp["error"] = f'Type "{self.group}"not found!'
        return resp
