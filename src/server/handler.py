import socket
import sys

import config as c

from . import utils

__all__ = ["readable", "writable", "errored"]


def readable(
    server: socket.socket, sockets: list[socket.socket]
) -> list[socket.socket]:
    if c.DEBUG:
        print(
            f"handler.readable: server={server.getsockname()} sockets={sockets.__len__()}",
            file=sys.stderr,
        )

    clients: list[socket.socket] = []

    for s in sockets:
        if s is server:
            if c.DEBUG:
                print("waiting for client accept...", file=sys.stderr)

            client, addr = s.accept()
            clients.append(client)

            if c.DEBUG:
                print(f"connected client from {addr}", file=sys.stderr)
        else:
            utils.handle_client_data(s, utils.read_from_client(s))
            if s.fileno() != -1:  # NOTE: append socket to clients if not closed
                clients.append(s)

    return clients


def writable(sockets: list[socket.socket]) -> list[socket.socket]:
    if c.DEBUG:
        print(
            f"handler.writable: sockets={sockets.__len__()}", file=sys.stderr)

    clients: list[socket.socket] = []

    for s in sockets:
        if c.DEBUG:
            print(f"socket writable s={s}", file=sys.stderr)

        s.close()

    return clients


def errored(sockets: list[socket.socket]) -> list[socket.socket]:
    if c.DEBUG:
        print(f"handler.errored: sockets={sockets.__len__()}", file=sys.stderr)

    clients: list[socket.socket] = []

    for s in sockets:
        if c.DEBUG:
            print(f"socket error: s={s}", file=sys.stderr)

        s.close()

    return clients
