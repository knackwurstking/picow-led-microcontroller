from typing import Callable

import config

__all__ = [
    "onchange",
    "start",
    "set_pin",
    "get_pin",
]

onchange: Callable[[int], None] | None = None


def start() -> None:
    """Starts the motion sensor service"""

    ...


def set_pin(number: int) -> None:
    """Changes the current motion sensor pin to use"""

    ...


def get_pin() -> int:
    """Returns the current motion sensor pin (-1 if disabled)"""

    ...
