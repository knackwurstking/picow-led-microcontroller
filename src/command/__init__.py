from . import config

__all__ = [
    "ALL_COMMANDS",
    "config",
    "run",
]

ALL_COMMANDS = [
    (config.SET_COLOR_PINS, config.set_color_pins),
    (config.GET_COLOR_PINS, config.get_color_pins),
]


def run(command: bytes, args: list[bytes]) -> None | list[bytes]:
    for cmd, fn in ALL_COMMANDS:
        if cmd == command:
            return fn(int(args[0]), args[1:])
