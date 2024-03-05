from dataclasses import dataclass

from . import config, info, led, motion

__all__ = [
    "COMMANDS",
    "run",
]


TYPE_GETTERS = "get"
TYPE_SETTERS = "set"
TYPE_EVENTS = "event"

GROUP_CONFIG = "config"
GROUP_INFO = "info"
GROUP_LED = "led"
GROUP_MOTION = "motion"


@dataclass
class Command:
    group: str
    type: str
    command: str

    def run(*args): ...


COMMANDS: list[Command] = [
    Command(GROUP_CONFIG, TYPE_SETTERS, "led"),
    Command(GROUP_CONFIG, TYPE_SETTERS, "motion"),
    Command(GROUP_CONFIG, TYPE_SETTERS, "motion-timeout"),
    Command(GROUP_CONFIG, TYPE_SETTERS, "pwm-range"),
    Command(GROUP_CONFIG, TYPE_GETTERS, "led"),
    Command(GROUP_CONFIG, TYPE_GETTERS, "motion"),
    Command(GROUP_CONFIG, TYPE_GETTERS, "motion-timeout"),
    Command(GROUP_CONFIG, TYPE_GETTERS, "pwm-range"),
    Command(GROUP_INFO, TYPE_GETTERS, "temp"),
    Command(GROUP_INFO, TYPE_GETTERS, "disk-usage"),
    Command(GROUP_INFO, TYPE_GETTERS, "version"),
    Command(GROUP_LED, TYPE_SETTERS, "duty"),
    Command(GROUP_LED, TYPE_GETTERS, "duty"),
    Command(GROUP_MOTION, TYPE_GETTERS, "duty"),
    Command(GROUP_MOTION, TYPE_EVENTS, "watch"),
]


@dataclass
class Response:
    id: int
    error: str | None
    data: any


def run(id: int, group: str, type: str, command: str, *args) -> Response:
    # TODO: iter commands and run, return response with/without error and data
    ...
