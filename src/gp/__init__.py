from . import gpled as gpled


def _init_led() -> gpled.GpLED:
    led = gpled.GpLED()

    cache = led.cache.read()
    if isinstance(cache, dict):
        if "pins" in cache:
            led.set_pins(*cache["pins"])

    return led


led: gpled.GpLED = _init_led()
