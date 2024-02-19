import logging
import socket

from . import callbacks

__all__ = ["read_from_client", "handle_client_data"]


def read_from_client(client: socket.socket) -> bytearray:
    logging.debug(f"client={client.getsockname()}")

    data: list[bytes] = []

    while True:
        chunk = client.recv(1)
        if chunk:
            if chunk == b"\n":
                break

            data.append(chunk)
        else:
            break

    return data


def handle_client_data(client: socket.socket, data: bytearray):
    logging.debug(f"client={client.getsockname()}, data={data}")

    if callbacks.ondata is not None and data.__len__() > 0:
        callbacks.ondata(client, data)
    elif data.__len__() == 0:
        client.close()


def response(client: socket.socket, data: bytearray):
    # NOTE: add a b"\n" at the end
    ...
