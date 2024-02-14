import socket
import sys

import config as c

from . import callbacks

__all__ = ["read_from_client", "handle_client_data"]


def read_from_client(client: socket.socket) -> list[bytes]:
    if c.DEBUG:
        print(
            f"read_from_client: client={client.getsockname()}", file=sys.stderr)

    data: list[bytes] = []

    while True:
        chunk = client.recv(1)
        if chunk:
            data.append(chunk)
        else:
            break

    return data


def handle_client_data(client: socket.socket, data: list[bytes]):
    if c.DEBUG:
        print(
            f"handle_client_data: client={client.getsockname()}, data={data}",
            file=sys.stderr,
        )

    if data.__len__() == 0:
        client.close()
        return

    if callbacks.ondata is not None:
        if callbacks.ondata(client, data):
            client.close()
    else:
        client.close()
        return
