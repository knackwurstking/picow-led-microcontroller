from . import led as _led


def _init_led() -> _led.GpLED:
    led = _led.GpLED()

    cache = led.cache.read()
    if isinstance(cache, dict):
        if "pins" in cache:
            led.set_pins(*cache.pins)

    return led


led: _led.GpLED = _init_led()
