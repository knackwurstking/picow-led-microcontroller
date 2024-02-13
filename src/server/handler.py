import sys
import socket

from . import utils

__all__ = [
    "readable",
    "writable",
    "errored"
]

def readable(server: socket.socket, sockets: list[socket.socket]) -> list[socket.socket]:
    print(f"handler.readable: server={server.getsockname()} sockets={sockets.__len__()}", file=sys.stderr)

    clients: list[socket.socket] = []

    for s in sockets:
        if s is server:
            print(f"waiting for client accept...", file=sys.stderr)
            client, addr = s.accept()
            clients.append(client)
            print(f"connected client from {addr}", file=sys.stderr)
        else:
            utils.handle_client_data(s, utils.read_from_client(s))
            s.close()

    return clients 

def writable(sockets: list[socket.socket]) -> list[socket.socket]:
    print(f"handler.writable: sockets={sockets.__len__()}", file=sys.stderr)

    clients: list[socket.socket] = []

    for s in sockets:
        print(f"socket writable s={s}", file=sys.stderr)
        s.close()

    return clients

def errored(sockets: list[socket.socket]) -> list[socket.socket]:
    print(f"handler.errored: sockets={sockets.__len__()}", file=sys.stderr)

    clients: list[socket.socket] = []

    for s in sockets:
        print(f"socket error: s={s}", file=sys.stderr)
        s.close()

    return clients