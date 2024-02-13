from typing import Callable

import sys
import select
import socket

__all__ = [
    "ondata",
    "start",
]

ondata: Callable[[socket.socket, list[bytes]], bool] | None = None

_readable_sockets: list[socket.socket] = []


def start(host: str, port: int = 0):
    server_socket = socket.socket()

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    _readable_sockets.append(server_socket)
    _start_main_loop(server_socket)


def _start_main_loop(server_socket: socket.socket):
    while True:
        print(f"Waiting for client...", file=sys.stderr)
        readable, writable, errored = select.select(
            _readable_sockets, [], [], 0.25
        )  # TODO: maybe find a better timeout value?

        _handle_readable(server_socket, readable)
        _handle_writable(writable)
        _handle_errored(errored)


def _handle_readable(server_socket: socket.socket, readable: list[socket.socket]):
    for s in readable:
        if s is server_socket:
            client, addr = s.accept()
            _readable_sockets.append(client)
            print(f"connected client from {addr}", file=sys.stderr)
        else:
            _handle_client_data(s, _read_from_client(s))


def _read_from_client(client: socket.socket) -> list[bytes]:
    data: list[bytes] = []

    while True:
        chunk = client.recv(1)
        if chunk:
            data.append(chunk)
        else:
            break

    return data


def _handle_client_data(client: socket.socket, data: list[bytes]):
    if data.__len__() == 0:
        return

    if ondata is not None:
        if ondata(client, data):
            _readable_sockets.remove(client)
    else:
        client.close()
        _readable_sockets.remove(client)


def _handle_writable(writable: list[socket.socket]):
    for s in writable:
        print(f"socket writable {s}", file=sys.stderr)

        s.close()
        _readable_sockets.remove(s)


def _handle_errored(errored: list[socket.socket]):
    for s in errored:
        print(f"socket error: {s}", file=sys.stderr)

        s.close()
        _readable_sockets.remove(s)
