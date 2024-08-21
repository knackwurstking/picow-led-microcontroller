import json
import logging
import socket

import config
import dc

from . import callbacks


def read_from_client(client: socket.socket):
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


def handle_client_data(client: socket.socket, data: bytes):
    logging.debug(f"client={client.getsockname()}, data={data!r}")

    if callbacks.ondata is not None and data.__len__() > 0:
        callbacks.ondata(client, data)
    else:
        client.close()


def response(client: socket.socket, response):
    client.settimeout(config.SOCKET_TIMEOUT_SEND)

    try:
        data = json.dumps(
            {
                "id": response.id,
                "error": response.error,
                "data": response.data,
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
