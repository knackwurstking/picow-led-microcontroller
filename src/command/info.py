from . import utils

__all__ = [
    "GET_TEMP",
    "GET_DISK_USAGE",
    "GET_VERSION",
    "get_temp",
    "get_disk_usage",
    "get_version",
]


GET_TEMP: int = int(0x21)
GET_DISK_USAGE: int = int(0x22)
GET_VERSION: int = int(0x23)


def get_temp(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    ...


def get_disk_usage(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    ...


def get_version(length: int, args: bytearray) -> bytearray:
    utils.validate_args(length, args, fixed=0)

    ...
