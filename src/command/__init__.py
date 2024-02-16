from . import config

__all__ = [
    "ALL_COMMANDS",
    "run",
    "config",
]

ALL_COMMANDS = [
    (config.SET_COLOR_PINS, config.set_color_pins),
    (config.GET_COLOR_PINS, config.get_color_pins),
    (config.SET_MOTION_PIN, config.set_motion_pin),
    (config.GET_MOTION_PIN, config.get_motion_pin),
    (config.SET_SERVER_ADDR, config.set_server_addr),
    (config.GET_SERVER_ADDR, config.get_server_addr),
    (config.SET_PWM_RANGE, config.set_pwm_range),
    (config.GET_PWM_RANGE, config.get_pwm_range),
]


def run(command: bytes, args: bytearray) -> None | bytearray:
    for cmd, fn in ALL_COMMANDS:
        if cmd == command:
            return fn(int(args[0]), args[1:])
