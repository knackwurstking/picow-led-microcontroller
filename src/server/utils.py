import json
import logging
import socket

import config
import dc

from . import callbacks

__all__ = ["read_from_client", "handle_client_data", "response"]


def read_from_client(client: socket.socket) -> bytes:
    logging.debug(f"client={client.getsockname()}")

    data: bytes = bytes()

    while True:
        chunk = client.recv(1)
        if chunk:
            if chunk == config.END_BYTE:
                break

            data += chunk
        else:
            break

    return data


def handle_client_data(client: socket.socket, data: bytes) -> None:
    logging.debug(f"client={client.getsockname()}, data={data!r}")

    if callbacks.ondata is not None and data.__len__() > 0:
        callbacks.ondata(client, data)


def response(client: socket.socket, resp: dc.Response) -> None:
    client.settimeout(config.SOCKET_TIMEOUT_SEND)

    try:
        data = json.dumps(
            {
                "id": resp.id,
                "error": resp.error,
                "data": resp.data,
            }
        )
        client.send(data.encode() + config.END_BYTE)
    except socket.timeout:
        pass
    except Exception as ex:
        logging.error(
            f'Exception while send response to client "{client.getsockname()}": {ex} [{type(ex)}]'  # noqa: E501
        )
        client.close()  # TODO: only close if exception is not a timeout?
    finally:
        client.settimeout(None)
