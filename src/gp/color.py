from __future__ import annotations
from typing import Callable

__all__ = [
    "onchange",
    "GpColor",
]

onchange: Callable[[list[int]], None] | None = None


class GpColor:
    _pins: list[int]

    def __init__(self, *pins) -> None:
        self._pins = list(pins)

    def set_pins(self, *pins: int) -> GpColor:
        self._pins = list(pins)
        return self

    def get_pins(self) -> list[int]:
        return self.pins
