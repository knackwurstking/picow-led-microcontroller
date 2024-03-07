from __future__ import annotations

from typing import Callable

__all__ = [
    "onchange",
    "GpMotion",
]

onchange: Callable[[int], None] | None = None


class GpMotion:
    _pin: int  # NOTE: use -1 to unset pin

    def __init__(self, pin) -> None:
        self._pin = pin

    def set_pin(self, pin: int) -> GpMotion:
        self._pin = pin
        return self

    def get_pin(self) -> int:
        return self.pin
