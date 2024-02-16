from . import utils

__all__ = [
    # commands
    "SET_COLOR_PINS",
    "GET_COLOR_PINS",
    "SET_MOTION_PIN",
    "GET_MOTION_PIN",
    "SET_SERVER_ADDR",
    "GET_SERVER_ADDR",
    "SET_PWM_RANGE",
    "GET_PWM_RANGE",
    # command handlers
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
    if not utils.validate_args(length, args, fixed=-1):
        return None

    pins: list[int] = []

    for arg in args:
        pins.append(int(arg))

    # TODO: run command
    ...


def get_color_pins(length: int, args: bytearray) -> None | bytearray:
    if not utils.validate_args(length, args, fixed=0):
        return None

    # TODO: run command and return bytearray
    ...

    return bytearray([GET_COLOR_PINS, 0x00])


def set_motion_pin(length: int, args: bytearray) -> None:
    if not utils.validate_args(length, args, fixed=1):
        return None

    ...


def get_motion_pin(length: int, args: bytearray) -> None | bytearray:
    if not utils.validate_args(length, args, fixed=0):
        return None

    ...


def set_server_addr(length: int, args: bytearray) -> None:
    if not utils.validate_args(length, args, fixed=-1):
        return None

    ...


def get_server_addr(length: int, args: bytearray) -> None | bytearray:
    if not utils.validate_args(length, args, fixed=0):
        return None

    ...


def set_pwm_range(length: int, args: bytearray) -> None:
    if not utils.validate_args(length, args, fixed=2):
        return None

    ...


def get_pwm_range(length: int, args: bytearray) -> None | bytearray:
    if not utils.validate_args(length, args, fixed=0):
        return None

    ...
