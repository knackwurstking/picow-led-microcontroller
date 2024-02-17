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
    if not utils.validate_args(length, args, fixed=-1):
        return None

    ...


def get_color_pins_duty(length: int, args: bytearray) -> None | bytearray:
    if not utils.validate_args(length, args, fixed=0):
        return None

    ...
