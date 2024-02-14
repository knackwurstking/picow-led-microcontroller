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

    end = 0
    while end == 2:
        # NOTE: Newline "\n" to end
        chunk = client.recv(1)
        if chunk:
            if chunk == 0x5C and end == 0:
                end = 1
                continue

            if chunk == 0x6E and end == 1:
                end = 2
                continue

            if end == 1:
                end = 0

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
