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

    def run(self, *args) -> dc.Response:
        resp = dc.Response(0, None, None)

        # TODO: kick this type shit (see led commands)
        if self.group == GROUP_CONFIG:
            return self.run_group_config(*args)

        if self.group == GROUP_INFO:
            return self.run_group_info(*args)

        if self.group == GROUP_LED:
            return self.run_group_led(*args)

        if self.group == GROUP_MOTION:
            return self.run_group_motion(*args)

        resp.error = f'Type "{self.group}"not found!'
        return resp

    def run_group_config(self, *args) -> dc.Response:
        if self.type == TYPE_SETTER:
            resp = config.run_setter(self.id, self.command, *args)
        elif self.type == TYPE_GETTER:
            resp = config.run_getter(self.id, self.command, *args)
        else:
            resp.error = f'Type "{self.type}"not found for group "{self.group}"!'

        return resp

    def run_group_info(self, *args) -> dc.Response:
        if self.type == TYPE_GETTER:
            resp = info.run_getter(self.id, self.command, *args)
        else:
            resp.error = f'Type "{self.type}"not found for group "{self.group}"!'

        return resp

    def run_group_led(self, *args) -> dc.Response:
        if self.type == TYPE_SETTER:
            resp = led.run_setter(self.id, self.command, *args)
        elif self.type == TYPE_GETTER:
            resp = led.run_getter(self.id, self.command, *args)
        else:
            resp.error = f'Type "{self.type}"not found for group "{self.group}"!'

        return resp

    def run_group_motion(self, *args) -> dc.Response:
        if self.type == TYPE_GETTER:
            resp = motion.run_getter(self.id, self.command, *args)
        elif self.type == TYPE_EVENT:
            resp = motion.run_event(self.id, self.command, *args)
        else:
            resp.error = f'Type "{self.type}"not found for group "{self.group}"!'

        return resp
