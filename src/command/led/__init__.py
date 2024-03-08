from typing import Callable

import dc

__all__ = ["run_setter", "run_getter"]


def set_duty(duty_cycle: int, pin: int | None = None) -> None:
    """Change the LED brightness (optional specify a specific pin,
    if not all pins are used)"""
    ...


def get_duty(*pins: int) -> int | None: ...


def run(id: int, _type: str, command: str, *args) -> dc.Response:
    response = dc.Response(id, None, None)

    run_command: Callable | None = None

    if command == "duty":
        if _type == "set":
            run_command = set_duty
        elif _type == "get":
            run_command = get_duty
        else:
            response.error = f'"{_type}" command "{command}" not found!'
    else:
        response.error = f'command "{command}" not found!'

    if run_command is None:
        return response

    try:
        response.data = run_command(*args)
    except Exception as ex:
        response.error = str(ex)

    return response
