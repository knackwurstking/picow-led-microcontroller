import sys
import select
import socket

from . import handler

__all__ = [
    "start",
]


def start(host: str, port: int = 0):
    server_socket = socket.socket()

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    main_loop(server_socket)


def main_loop(server_socket: socket.socket):
    readable_sockets = []
    writable_sockets = []
    errored_sockets = []

    while True:
        print(f"Waiting for client... [server_socket={server_socket.getsockname()}]", end="\r", file=sys.stderr)

        if readable_sockets.__len__() == 0:
            readable_sockets.append(server_socket)

        readable, writable, errored = select.select(
            readable_sockets, writable_sockets, errored_sockets, 0.25
        )

        if readable.__len__() == 0 and writable.__len__() == 0 and errored.__len__() == 0:
            continue

        print(file=sys.stderr)

        readable_sockets = handler.readable(server_socket, readable)
        writable_sockets = handler.writable(writable)
        errored_sockets = handler.errored(errored)