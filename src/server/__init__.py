import select
import socket
import time
from sys import stderr

import config

from . import callbacks, handler, utils

event_sockets: list[socket.socket] = []


def start(host: str, port: int = 0):
    server_socket = socket.socket()

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    main_loop(server_socket)


def main_loop(server_socket: socket.socket):
    readable_sockets: list[socket.socket] = []

    while True:
        if readable_sockets.__len__() == 0:
            readable_sockets.append(server_socket)

        try:
            readable, writable, errored = select.select(
                readable_sockets,
                [],
                [],
                config.SOCKET_TIMEOUT_SELECT,
            )
        except Exception as ex:
            print(
                f'[ERROR] Got an exception while running select.select: "{ex}"',  # noqa: E501
                file=stderr,
            )

            # Remove dead sockets
            for s in readable_sockets.copy():
                print(
                    f"[DEBUG] Remove socket {s} from readable_sockets",
                    file=stderr,
                )
                readable_sockets.remove(s)

            time.sleep(1)
            continue

        if readable.__len__() > 0:
            readable_sockets = handler.readable(server_socket, readable)

        if writable.__len__() > 0:
            print(
                f"[DEBUG] There are writable sockets ({writable.__len__()})",
                file=stderr,
            )

        if errored.__len__() > 0:
            handler.errored(errored)
