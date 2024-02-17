from . import utils

__all__ = [
    "GET_MOTION_DATA",
]

GET_MOTION_DATA: int = int(0x61)


def get_motion_data(length: int, args: bytearray) -> None:
    if not utils.validate_args(length, args, fixed=-1):
        return None

    ...
