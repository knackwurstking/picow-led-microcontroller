from dataclasses import dataclass
import logging

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
GROUP_motion = "motion"


@dataclass
class Command:
    group: str
    type: str
    command: str

    def run(*args): ...


# TODO: update commands...
COMMANDS: list[Command] = [
    # group config setters
    Command(GROUP_CONFIG, TYPE_SETTERS, "led"),
    Command(GROUP_CONFIG, TYPE_SETTERS, "motion"),
    Command(GROUP_CONFIG, TYPE_SETTERS, "motion-timeout"),
    Command(GROUP_CONFIG, TYPE_SETTERS, "pwm-range"),
    # group config getters
    Command(GROUP_CONFIG, TYPE_GETTERS, "led"),
    Command(GROUP_CONFIG, TYPE_GETTERS, "motion"),
    Command(GROUP_CONFIG, TYPE_GETTERS, "motion-timeout"),
    Command(GROUP_CONFIG, TYPE_GETTERS, "pwm-range"),
    # group info getters
    Command(GROUP_INFO, TYPE_GETTERS, "temp"),
    Command(GROUP_INFO, TYPE_GETTERS, "disk-usage"),
    Command(GROUP_INFO, TYPE_GETTERS, "version"),
    # TODO: group led setters
    # TODO: group led getters
    # TODO: group motion getters
    # TODO: group motion events
]


@dataclass
class Response:
    id: int
    error: str | None
    data: any


def run(id: int, group: str, type: str, command: str, *args) -> Response:
    # TODO: iter commands and run, return response with/without error and data
    ...
