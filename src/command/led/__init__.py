from typing import Union

from ... import dc

__all__ = ["run_setter", "run_getter"]


def set_duty(duty_cycle: int, pin: int) -> None: ...


def get_duty(*pins: int) -> int | None: ...


def run_setter(id: int, command: str, *args) -> dc.Response:
    response = dc.Response(id, None, None)

    run_command = None

    if command == "duty":
        run_command = set_duty
    else:
        response.error = f'Command "{command}" not found!'
        return response

    try:
        response.data = run_command(*args)
    except Exception as ex:
        response.error = str(ex)

    return response


def run_getter(id: int, command: str, *args) -> dc.Response:
    response = dc.Response(id, None, None)

    run_command = None

    if command == "duty":
        run_command = get_duty
    else:
        response.error = f'Command "{command}" not found!'
        return response

    try:
        response.data = run_command(*args)
    except Exception as ex:
        response.error = str(ex)

    return response
