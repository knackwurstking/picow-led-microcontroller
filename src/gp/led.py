from __future__ import annotations

from typing import Callable, Tuple

from cache import Cache
import config


onchange: Callable[[list[int]], None] | None = None


class GpLED:
    _pins: list[int]
    _pwm_range: Tuple[int, int]

    def __init__(
        self,
        *pins,
        pwm_range_min: int = config.LED_PWM_RANGE_MIN,
        pwm_range_max: int = config.LED_PWM_RANGE_MAX,
    ) -> None:
        self.cache = Cache("gp-led")  # TODO: ...
        self._pins = list(pins)
        self._pwm_range = (pwm_range_min, pwm_range_max)

    def set_pins(self, *pins: int) -> GpLED:
        # TODO: cache this to the pico device
        self._pins = list(pins)
        return self

    def get_pins(self) -> list[int]:
        return self._pins

    def has_pin(self, pin: int) -> bool:
        for pin in self._pins:
            if pin == pin:
                return True

        return False

    def set_pwm_range(self, min: int, max: int) -> GpLED:
        # TODO: cache this to the pico device
        self._pwm_range = (min, max)
        return self

    def get_pwm_range(self) -> Tuple[int, int]:
        return self._pwm_range

    def set_duty(self, cycle: int): ...

    def get_duty(self) -> list[int]:
        ...

        return []

    def set_pin_duty(self, pin: int, cycle: int): ...

    def get_pin_duty(self, pin: int) -> int:
        # TODO: get the current dutycycle for the given pin
        raise Exception(f'pin "{pin}" not found!')
