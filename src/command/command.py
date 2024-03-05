from dataclasses import dataclass

from . import config, info, led, motion
from .response import Response

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

    def run(self, *args) -> Response:
        response = Response(0, None, None)

        if self.group == GROUP_CONFIG:
            if self.type == TYPE_SETTER:
                response = config.run_setter(self.command, *args)
            elif self.type == TYPE_GETTER:
                response = config.run_getter(self.command, *args)
            else:
                response.error = (
                    f'Type "{self.type}"not found for group "{self.group}"!'
                )

            return response

        if self.group == GROUP_INFO:
            if self.type == TYPE_GETTER:
                response = info.run_getter(self.command, *args)
            else:
                response.error = (
                    f'Type "{self.type}"not found for group "{self.group}"!'
                )

            return response

        if self.group == GROUP_LED:
            if self.type == TYPE_SETTER:
                response = led.run_setter(self.command, *args)
            elif self.type == TYPE_GETTER:
                response = led.run_getter(self.command, *args)
            else:
                response.error = (
                    f'Type "{self.type}"not found for group "{self.group}"!'
                )

            return response

        if self.group == GROUP_MOTION:
            if self.type == TYPE_GETTER:
                response = motion.run_getter(self.command, *args)
            elif self.type == TYPE_EVENT:
                response = motion.run_event(self.command, *args)
            else:
                response.error = (
                    f'Type "{self.type}"not found for group "{self.group}"!'
                )

            return response

        response.error = f'Type "{self.group}"not found!'
        return response
