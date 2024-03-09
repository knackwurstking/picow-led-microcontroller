import socket
from typing import Callable

import dc
import server

__all__ = ["run"]


def event_start(client: socket.socket) -> None:
    server.event_sockets.append(client)


def event_stop(client: socket.socket) -> None:
    server.event_sockets.remove(client)


def run(client: socket.socket, id: int, _type: str, command: str, *args) -> dc.Response:
    response = dc.Response(id, None, None)
    run_command: Callable | None = None

    if _type == "event":
        try:
            run_command = get_event_command(command)
        except Exception as ex:
            response.error = str(ex)
    else:
        response.error = f'"{_type}" command "{command}" not found!'

    if run_command is None:
        return response

    try:
        if _type == "event":
            response.data = run_command(client)
        else:
            response.data = run_command(*args)
    except Exception as ex:
        response.error = str(ex)

    return response


def get_event_command(command: str) -> Callable | None:
    run_command: Callable | None = None

    if command == "start":
        run_command = event_start
    elif command == "stop":
        run_command = event_stop
    else:
        raise Exception(f'command "{command}" not found!')

    return run_command
