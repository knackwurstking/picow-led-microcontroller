from . import led as _led
from . import motion as _motion

__all__ = [
    "led",
    "motion",
]


def _init_led() -> _led.GpLED:
    global led
    led = _led.GpLED()  # TODO: set cached pins
    return led


def _init_motion() -> _motion.GpMotion:
    global motion
    motion = _motion.GpMotion()  # TODO: set cached pin
    return motion


led: _led.GpLED = _init_led()
motion: _motion.GpMotion = _init_motion()
