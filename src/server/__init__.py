from typing import Callable

import sys
import select
import socket

# NOTE: Don't forget to close the socket
ondata: Callable[[socket.socket, list[bytes]]] | None = None

_readable_sockets: list[socket.socket] = []


def start():
    server_socket = socket.socket()
    _readable_sockets.append(server_socket)
    _start_main_loop(server_socket)


def _start_main_loop(server_socket: socket.socket):
    while True:
        readable, __writable__, errored = select.select(
            _readable_sockets, [], [], 0
        )  # TODO: maybe find a better timeout value?

        _handle_readable(server_socket, readable)
        _handle_errored(errored)


def _handle_readable(server_socket: socket.socket, readable: list[socket.socket]):
    for sock in readable:
        if sock is server_socket:
            client, __addr__ = server_socket.accept()
            _readable_sockets.append(client)
        else:
            _handle_client_data(sock, _read_from_client(sock))


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
        ondata(client, data)
    else:
        client.close()
        _readable_sockets.remove(client)


def _handle_errored(errored: list[socket.socket]):
    for s in errored:
        print(f"socket error: {s}", file=sys.stderr)
        s.close()
