from dataclasses import dataclass

from . import config, info, led, motion

__all__ = [
    "run",
]


TYPE_GETTER = "get"
TYPE_SETTER = "set"
TYPE_EVENT = "event"

GROUP_CONFIG = "config"
GROUP_INFO = "info"
GROUP_LED = "led"
GROUP_MOTION = "motion"


@dataclass
class Response:
    id: int
    error: str | None
    data: any


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
            elif self.type == TYPE_EVENT:
                response = config.run_event(self.command, *args)
            else:
                response.error = f'Type "{self.type}"not found!'

            return response

        if self.group == GROUP_INFO:
            if self.type == TYPE_GETTER:
                response = info.run_getter(self.command, *args)
            else:
                response.error = f'Type "{self.type}"not found!'

            return response

        if self.group == GROUP_LED:
            if self.type == TYPE_SETTER:
                response = led.run_setter(self.command, *args)
            elif self.type == TYPE_GETTER:
                response = led.run_getter(self.command, *args)
            else:
                response.error = f'Type "{self.type}"not found!'

            return response

        if self.group == GROUP_MOTION:
            if self.type == TYPE_GETTER:
                response = motion.run_getter(self.command, *args)
            elif self.type == TYPE_EVENT:
                response = motion.run_event(self.command, *args)
            else:
                response.error = f'Type "{self.type}"not found!'

            return response

        response.error = f'Type "{self.group}"not found!'
        return response


def run(id: int, group: str, type: str, command: str, *args) -> Response:
    return Command(id, group, type, command).run()
