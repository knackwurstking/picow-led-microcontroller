import logging
import socket

import config

from . import callbacks

__all__ = ["read_from_client", "handle_client_data", "response"]


def read_from_client(client: socket.socket) -> bytearray:
    logging.debug(f"client={client.getsockname()}")

    data: list[bytes] = []

    while True:
        chunk = client.recv(1)
        if chunk:
            if chunk == config.END_BYTE:
                break

            data.append(chunk)
        else:
            client.close()
            break

    return data


def handle_client_data(client: socket.socket, data: bytearray):
    logging.debug(f"client={client.getsockname()}, data={data}")

    if callbacks.ondata is not None and data.__len__() > 0:
        callbacks.ondata(client, data)


def response(client: socket.socket, data: bytearray):
    client.settimeout(config.SOCKET_TIMEOUT_SEND)
    try:
        client.send(data + config.END_BYTE)
    except Exception as ex:
        logging.error(
            f'Exception while send response to client "{client.getsockname()}": {ex} [{type(ex)}]'  # noqa: E501
        )
    finally:
        client.settimeout(None)
