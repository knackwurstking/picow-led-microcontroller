from __future__ import annotations

from typing import Callable

import config

__all__ = [
    "onchange",
    "GpLED",
]

onchange: Callable[[list[int]], None] | None = None


class GpLED:
    _pins: list[int]
    _pwm_range: list[int, int]

    def __init__(
        self,
        *pins,
        pwm_range_min: int = config.LED_PWM_RANGE_MIN,
        pwm_range_max: int = config.LED_PWM_RANGE_MAX,
    ) -> None:
        self._pins = list(pins)
        self._pwm_range = [pwm_range_min, pwm_range_max]

    def set_pins(self, *pins: int) -> GpLED:
        self._pins = list(pins)
        return self

    def get_pins(self) -> list[int]:
        return self.pins

    def set_pwm_range(self, min: int, max: int) -> GpLED:
        # TODO: cache this to the pico device
        self._pwm_range = [min, max]
        return self

    def get_pwm_range(self) -> list[int, int]:
        return self._pwm_range
