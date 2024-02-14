import select
import socket
import sys
import time

import wifi

import config as c

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
        if c.DEBUG:
            print(
                f"Waiting for client... [server_socket={server_socket.getsockname()}]",
                end="\r",
                file=sys.stderr,
            )

        if readable_sockets.__len__() == 0:
            readable_sockets.append(server_socket)

        if not wifi.check():
            try:
                wifi.connect()
            except Exception as ex:
                # TODO: do a machine reset
                ...

                if c.DEBUG:
                    print(
                        f"exception wile thying to connect to wifi: {ex}",
                        file=sys.stderr,
                    )

                time.sleep(5)

        try:
            readable_sockets, writable_sockets, errored_sockets = select.select(
                readable_sockets, writable_sockets, errored_sockets, 0.25
            )
        except Exception as ex:
            if c.DEBUG:
                print(
                    f"got an exception while running select.select: {ex}",
                    file=sys.stderr,
                )

            continue

        if (
            readable_sockets.__len__() == 0
            and writable_sockets.__len__() == 0
            and errored_sockets.__len__() == 0
        ):
            continue

        if c.DEBUG:
            print(file=sys.stderr)

        readable_sockets = handler.readable(server_socket, readable_sockets)
        writable_sockets = handler.writable(writable_sockets)
        errored_sockets = handler.errored(errored_sockets)