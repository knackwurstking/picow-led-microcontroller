from typing import Callable

import dc
import config

__all__ = ["run"]


def get_temp() -> float: ...


def get_disk_usage() -> dict[str, int]: ...


def get_version() -> str:
    return config.VERSION


def run(id: int, _type: str, command: str, *args) -> dc.Response:
    response = dc.Response(id, None, None)
    run_command: Callable | None = None

    if _type == "get":
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


def get_getter_command(command: str) -> Callable | None:
    run_command: Callable | None = None

    if command == "temp":
        run_command = get_temp
    elif command == "disk-usage":
        run_command = get_disk_usage
    elif command == "version":
        run_command = get_version
    else:
        raise Exception(f'command "{command}" not found!')

    return run_command
