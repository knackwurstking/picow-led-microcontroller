from __future__ import annotations

from typing import Callable

__all__ = [
    "onchange",
    "GpMotion",
]

onchange: Callable[[int], None] | None = None


class GpMotion:
    _pin: int  # NOTE: use -1 to unset pin
    _motion_timeout: int  # NOTE: resets the timer

    def __init__(self, pin: int = -1, motion_timeout: int = 60000) -> None:
        self._pin = pin
        self._motion_timeout = motion_timeout

    def set_pin(self, pin: int) -> GpMotion:
        """Set the motion sensor Gp Pin, disable with -1"""
        # TODO: update local config (save to pico)
        self._pin = pin
        return self

    def get_pin(self) -> int:
        """Returns the current motion sensor pin in use (-1 means its disabled)"""
        return self.pin

    def set_motion_timeout(self, value: int) -> None:
        # TODO: update local config (save to pico)
        self.set_motion_timeout = value

    def get_motion_timeout(self, value: int) -> int:
        return self._motion_timeout
