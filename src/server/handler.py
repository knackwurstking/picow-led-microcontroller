import socket
from sys import stderr

from . import utils


def readable(
    server: socket.socket, sockets: list[socket.socket]
) -> list[socket.socket]:
    clients: list[socket.socket] = []

    for s in sockets:
        if s is server:
            print("[DEBUG] Waiting for client accept...", file=stderr)

            client, addr = s.accept()
            clients.append(client)

            print(f"[DEBUG] Connected client from {addr}", file=stderr)
        else:
            data = utils.read_from_client(s)

            if s.fileno() == -1:
                continue

            utils.handle_client_data(s, data)

            # NOTE: append socket to clients if not closed
            print(f"[DEBUG] socket fileno: {s.fileno()}", file=stderr)
            if s.fileno() != -1:
                clients.append(s)

    return clients


def errored(sockets: list[socket.socket]) -> None:
    print(f"[DEBUG] sockets={len(sockets)}", file=stderr)

    for s in sockets:
        print(f"[DEBUG] Socket error: s={s}", file=stderr)
        s.close()
