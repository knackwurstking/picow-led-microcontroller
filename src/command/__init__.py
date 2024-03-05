import logging
from dataclasses import dataclass

from . import config, info, led, motion

__all__ = [
    "COMMANDS",
    "run",
]

# TODO: update commands...
COMMANDS = [
    (config.SET_COLOR_PINS, config.set_color_pins, "config.set_color_pins"),
    (config.GET_COLOR_PINS, config.get_color_pins, "config.get_color_pins"),
    (config.SET_MOTION_PIN, config.set_motion_pin, "config.set_motion_pin"),
    (config.GET_MOTION_PIN, config.get_motion_pin, "config.get_motion_pin"),
    (
        config.SET_MOTION_TIMEOUT,
        config.set_motion_timeout,
        "config.set_motion_timeout",
    ),
    (
        config.GET_MOTION_TIMEOUT,
        config.get_motion_timeout,
        "config.get_motion_timeout",
    ),
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


@dataclass
class Response:
    id: int
    error: str | None
    data: any


def run(id: int, group: str, type: str, command: str, *args) -> Response:
    # TODO: iter commands and run, return response with/without error and data
