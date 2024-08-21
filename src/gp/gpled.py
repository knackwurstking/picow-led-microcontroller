from cache import Cache
import config


# ((data: int[] | None) => void) | None
onchange = None


class GpLED:
    _pins: list[int]
    _pwm_range: tuple[int, int]

    def __init__(
        self,
        *pins,
        pwm_range_min: int = config.LED_PWM_RANGE_MIN,
        pwm_range_max: int = config.LED_PWM_RANGE_MAX,
    ) -> None:
        self.cache = Cache("gp-led")
        self._pins = list(pins)
        self._pwm_range = (pwm_range_min, pwm_range_max)

    def set_pins(self, *pins: int):
        # TODO: cache this to the pico device
        self._pins = list(pins)

    def get_pins(self) -> list[int]:
        return self._pins

    def has_pin(self, pin: int) -> bool:
        for pin in self._pins:
            if pin == pin:
                return True

        return False

    def set_pwm_range(self, min: int, max: int):
        # TODO: cache this to the pico device
        self._pwm_range = (min, max)

    def get_pwm_range(self) -> tuple[int, int]:
        return self._pwm_range

    def set_duty(self, cycle: int): ...

    def get_duty(self) -> list[int]:
        ...

        return []

    def set_pin_duty(self, pin: int, cycle: int): ...

    def get_pin_duty(self, pin: int) -> int:
        # TODO: get the current dutycycle for the given pin
        raise Exception(f'pin "{pin}" not found!')
