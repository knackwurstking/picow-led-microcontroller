__all__ = [
    "validate_args",
]

ARGS_ERROR = Exception("args error")


def validate_args(length: int, args: bytearray, fixed=-1):
    if fixed < 0:
        if args.__len__() != length:
            raise ARGS_ERROR

        return

    if args.__len__() != length or length != fixed:
        raise ARGS_ERROR
