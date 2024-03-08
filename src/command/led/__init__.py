from typing import Callable

import dc
import gp

__all__ = ["run"]


def set_duty(duty_cycle: int, pin: int | None = None) -> None:
    """Change the LED brightness (optional specify a specific pin,
    if not all pins are used)"""
    if pin is None or pin < 0:
        # TODO: set duty for all pins
        ...
    else:
        # TODO: set duty for a specific pin
        ...


def get_duty(pin: int | None = None) -> list[int] | int | None:
    if pin is None:
        return gp.led.get_duty()

    if pin < 0:
        return gp.led.get_duty()

    if gp.led.has_pin(pin):
        return gp.led.get_pin_duty(pin)

    return None


def run(id: int, _type: str, command: str, *args) -> dc.Response:
    response = dc.Response(id, None, None)
    run_command: Callable | None = None

    if _type == "set":
        try:
            run_command = set_duty
        except Exception as ex:
            response.error = str(ex)
    elif _type == "get":
        try:
            run_command = get_duty
        except Exception as ex:
            response.error = str(ex)
    else:
        response.error = f'"{_type}" command "{command}" not found!'

    if run_command is None:
        return response

    try:
        response.data = run_command(*args)
    except Exception as ex:
        response.error = str(ex)

    return response


def get_setter_command(command: str) -> Callable | None:
    run_command: Callable | None = None

    if command == "duty":
        run_command = set_duty
    else:
        raise Exception(f'command "{command}" not found!')

    return run_command


def get_getter_command(command: str) -> Callable | None:
    run_command: Callable | None = None

    if command == "duty":
        run_command = get_duty
    else:
        raise Exception(f'command "{command}" not found!')

    return run_command
