from typing import Tuple, Callable
import dc
import gp


def set_led_pins(*pins: int) -> None:
    for pin in list(pins):
        if not isinstance(pin, int):
            raise Exception(f"all pins need to be from type {type(int)}")

        if pin < 0:
            raise Exception("led pins have to be positive")

    gp.led.set_pins(*pins)


def get_led_pins() -> list[int]:
    return gp.led.get_pins()


def set_pwm_range(min: int, max: int) -> None:
    if not isinstance(min, int) or not isinstance(max, int):
        raise Exception(f"min/max needs to be from type {type(int)}")

    gp.led.set_pwm_range(min, max)


def get_pwm_range() -> Tuple[int, int]:
    return gp.led.get_pwm_range()


def run(id: int, _type: str, command: str, *args) -> dc.Response:
    response = dc.Response(id, None, None)
    run_command: Callable | None = None

    if _type == "set":
        try:
            run_command = get_setter_command(command)
        except Exception as ex:
            response.error = str(ex)
    elif _type == "get":
        try:
            run_command = get_getter_command(command)
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

    if command == "led":
        run_command = set_led_pins
    elif command == "pwm-range":
        run_command = set_pwm_range
    else:
        raise Exception(f'command "{command}" not found!')

    return run_command


def get_getter_command(command: str) -> Callable | None:
    run_command: Callable | None = None

    if command == "led":
        run_command = get_led_pins
    elif command == "pwm-range":
        run_command = get_pwm_range
    else:
        raise Exception(f'command "{command}" not found!')

    return run_command
