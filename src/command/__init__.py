import logging

from . import config, info, led, motion

__all__ = [
    "ALL_COMMANDS",
    "run",
    "config",
]

ALL_COMMANDS = [
    (config.SET_COLOR_PINS, config.set_color_pins, "config.set_color_pins"),
    (config.GET_COLOR_PINS, config.get_color_pins, "config.get_color_pins"),
    (config.SET_MOTION_PIN, config.set_motion_pin, "config.set_motion_pin"),
    (config.GET_MOTION_PIN, config.get_motion_pin, "config.get_motion_pin"),
    (config.SET_SERVER_ADDR, config.set_server_addr, "config.set_server_addr"),
    (config.GET_SERVER_ADDR, config.get_server_addr, "config.get_server_addr"),
    (config.SET_PWM_RANGE, config.set_pwm_range, "config.set_pwm_range"),
    (config.GET_PWM_RANGE, config.get_pwm_range, "config.get_pwm_range"),
    (info.GET_TEMP, info.get_temp, "info.get_temp"),
    (info.GET_DISK_USAGE, info.get_disk_usage, "info.get_disk_usage"),
    (info.GET_VERSION, info.get_version, "info.get_version"),
    (
        led.SET_COLOR_PINS_DUTY,
        led.set_color_pins_duty,
        "led.set_color_pins_duty",
    ),
    (
        led.GET_COLOR_PINS_DUTY,
        led.get_color_pins_duty,
        "led.get_color_pins_duty",
    ),
    (motion.GET_MOTION_DATA, motion.get_motion_data, "motion.get_motion_data"),
]


def run(command: bytes, args: bytearray) -> None | bytearray:
    for cmd, fn, name in ALL_COMMANDS:
        if cmd == command:
            logging.debug(f'Run command "{name}"...')
            return fn(int(args[0]), args[1:])
