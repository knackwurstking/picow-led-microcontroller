from typing import Callable

import dc

__all__ = ["run"]


def get_last_motion() -> int | None: ...


def event_watch_motions(host: str, port: int) -> ...: ...


def run(id: int, _type: str, command: str, *args) -> dc.Response:
    response = dc.Response(id, None, None)
    run_command: Callable | None = None

    if _type == "get":
        try:
            run_command = get_getter_command(command)
        except Exception as ex:
            response.error = str(ex)
    elif _type == "event":
        try:
            run_command = get_event_command(command)
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


def get_getter_command(command: str) -> Callable | None:
    run_command: Callable | None = None

    if command == "last-motion":
        run_command = get_last_motion
    else:
        raise Exception(f'command "{command}" not found!')

    return run_command


def get_event_command(command: str) -> Callable | None:
    run_command: Callable | None = None

    if command == "watch-motions":
        run_command = event_watch_motions
    else:
        raise Exception(f'command "{command}" not found!')

    return run_command
