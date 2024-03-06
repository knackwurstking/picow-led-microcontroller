from __future__ import annotations
from typing import Callable

__all__ = [
    "onchange",
    "GpLED",
]

onchange: Callable[[list[int]], None] | None = None


class GpLED:
    _pins: list[int]

    def __init__(self, *pins) -> None:
        self._pins = list(pins)

    def set_pins(self, *pins: int) -> GpLED:
        self._pins = list(pins)
        return self

    def get_pins(self) -> list[int]:
        return self.pins
