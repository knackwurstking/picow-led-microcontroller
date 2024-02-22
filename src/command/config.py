from gp import color, motion

from . import utils

__all__ = [
    "SET_COLOR_PINS",
    "GET_COLOR_PINS",
    "SET_MOTION_PIN",
    "GET_MOTION_PIN",
    "SET_SERVER_ADDR",
    "GET_SERVER_ADDR",
    "SET_PWM_RANGE",
    "GET_PWM_RANGE",
    "set_color_pins",
    "get_color_pins",
    "set_motion_pin",
    "get_motion_pin",
    "set_server_addr",
    "get_server_addr",
    "set_pwm_range",
    "get_pwm_range",
]

SET_COLOR_PINS: int = int(0x01)
GET_COLOR_PINS: int = int(0x02)

SET_MOTION_PIN: int = int(0x03)
GET_MOTION_PIN: int = int(0x04)

SET_SERVER_ADDR: int = int(0x05)
GET_SERVER_ADDR: int = int(0x06)

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

    # TODO: run command and return bytearray
    ...

    return bytearray([GET_COLOR_PINS, 0x00])


def set_motion_pin(length: int, args: bytearray) -> None:
    utils.validate_args(length, args, fixed=1)

    ...


def get_motion_pin(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    ...


def set_server_addr(length: int, args: bytearray) -> None:
    utils.validate_args(length, args, fixed=-1)

    ...


def get_server_addr(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    ...


def set_pwm_range(length: int, args: bytearray) -> None:
    utils.validate_args(length, args, fixed=2)

    ...


def get_pwm_range(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    ...
