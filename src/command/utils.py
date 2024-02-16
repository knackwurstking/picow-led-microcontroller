__all__ = [
    "validate_args",
]


def validate_args(length: int, args: bytearray, fixed=-1) -> bool:
    if fixed < 0:
        return args.__len__() == length

    return args.__len__() == length and length == fixed
