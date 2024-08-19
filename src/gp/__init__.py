from . import led as _led


def _init_led() -> _led.GpLED:
    global led
    led = _led.GpLED()  # TODO: set cached pins
    return led


led: _led.GpLED = _init_led()
