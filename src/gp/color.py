from typing import Callable

import config

__all__ = [
    "onchange",
    "start",
    "set_pins",
    "get_pins",
]

onchange: Callable[[*int], None] | None = None


def start() -> None:
    """Starts the color service"""

    ...


def set_pins(*pins: int) -> None:
    """Changes the current color pins to use"""

    ...


def get_pins() -> list[int]:
    """Returns the current color pins"""

    ...
