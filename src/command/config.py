__all__ = [
    "SET_COLOR_PINS",
    "GET_COLOR_PINS",
    "set_color_pins",
    "get_color_pins",
]

SET_COLOR_PINS: bytes = 0x01
GET_COLOR_PINS: bytes = 0x02


def set_color_pins(length: int, args: list[bytes]) -> None:
    if args.__len__() != length:
        return None

    pins: list[int] = []

    for arg in args:
        pins.append(int(arg))

    # TODO: run command
    ...


def get_color_pins(length: int, args: list[bytes]) -> None | list[bytes]:
    if args.__len__() != length or length != 0:
        return False

    # TODO: run command and return bytearray
    ...

    return [GET_COLOR_PINS, 0x00]
