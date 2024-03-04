from gp import color, motion

from . import utils

__all__ = [
    "SET_COLOR_PINS",
    "GET_COLOR_PINS",
    "SET_MOTION_PIN",
    "GET_MOTION_PIN",
    "SET_MOTION_TIMEOUT",
    "GET_MOTION_TIMEOUT",
    "SET_PWM_RANGE",
    "GET_PWM_RANGE",
    "set_color_pins",
    "get_color_pins",
    "set_motion_pin",
    "get_motion_pin",
    "set_motion_timeout",
    "get_motion_timeout",
    "set_pwm_range",
    "get_pwm_range",
]

SET_COLOR_PINS: int = int(0x01)
GET_COLOR_PINS: int = int(0x02)

SET_MOTION_PIN: int = int(0x03)
GET_MOTION_PIN: int = int(0x04)

SET_MOTION_TIMEOUT: int = int(0x05)
GET_MOTION_TIMEOUT: int = int(0x06)

SET_PWM_RANGE: int = int(0x07)
GET_PWM_RANGE: int = int(0x08)


def set_color_pins(length: int, args: bytearray) -> None:
    utils.validate_args(length, args, fixed=-1)

    pins: list[int] = []

    for arg in args:
        pins.append(int(arg))

    color.set_pins(*pins)


def get_color_pins(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    pins = color.get_pins()

    return bytearray([GET_COLOR_PINS, pins.__len__()] + pins)


def set_motion_pin(length: int, args: bytearray) -> None:
    utils.validate_args(length, args, fixed=1)

    motion.set_pin(int(args[0]))


def get_motion_pin(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    pin = motion.get_Pin()
    if pin is None:
        return bytearray([GET_MOTION_PIN, 0x00])

    return bytearray([GET_MOTION_PIN, 0x01, pin])


def set_motion_timeout(length: int, args: bytearray) -> None:
    utils.validate_args(length, args, fixed=-1)

    # TODO: convert args to string
    ...


def get_motion_timeout(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    ...


def set_pwm_range(length: int, args: bytearray) -> None:
    utils.validate_args(length, args, fixed=2)

    ...


def get_pwm_range(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    ...
