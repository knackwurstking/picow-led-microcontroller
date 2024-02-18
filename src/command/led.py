from . import utils

__all__ = [
    "SET_COLOR_PINS_DUTY",
    "GET_COLOR_PINS_DUTY",
    "set_color_pins_duty",
    "get_color_pins_duty",
]


SET_COLOR_PINS_DUTY: int = int(0x41)
GET_COLOR_PINS_DUTY: int = int(0x42)


def set_color_pins_duty(length: int, args: bytearray) -> None:
    utils.validate_args(length, args, fixed=-1)

    ...


def get_color_pins_duty(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    ...
