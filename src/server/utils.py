import json
import socket
from sys import stderr

import config

from . import callbacks


def read_from_client(client: socket.socket):
    print(f"[DEBUG] client={client.getsockname()}", file=stderr)

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
    print(f"[DEBUG] client={client.getsockname()}, data={data!r}", file=stderr)

    if callbacks.ondata is not None and len(data) > 0:
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
        print(
            f'[ERROR] Exception while send response to client "{client.getsockname()}": {ex} [{type(ex)}]',  # noqa: E501
            file=stderr,
        )
        client.close()  # TODO: only close if exception is not a timeout?
    finally:
        client.settimeout(None)
