from ..response import Response
import gp

__all__ = ["run_setter", "run_getter"]


def set_led_pins(*pins: int) -> None:
    gp.led.set_pins(*pins)


def get_led_pins() -> list[int]:
    return gp.led.get_pins()


def set_motion_pin(pin: int) -> None: ...


def get_motion_pin() -> int | None: ...


def set_motion_timeout_value(timeout: int) -> None: ...


def get_motion_timeout_value() -> int: ...


def set_pwm_range(min: int, max: int) -> None: ...


def get_pwm_range() -> list[int, int]: ...


def run_setter(id: int, command: str, *args) -> Response:
    response = Response(id, None, None)

    if command == "led":
        response.data = set_led_pins(id, *args)
    else:
        response.error = f'Command "{command}" not found!'

    return response


def run_getter(id: int, command: str, *args) -> Response:
    response = Response(id, None, None)

    if command == "led":
        response.data = get_led_pins(id)
    else:
        response.error = f'Command "{command}" not found!'

    return response
