import logging
import socket
import json

import command
import config as c
import server
from server.utils import response
from . import dc


def ondata(client: socket.socket, data: bytearray):
    logging.debug(f"client={client.getsockname()}, data={data}")

    req_raw: any = None

    try:
        req_raw = json.loads(data)
    except Exception:
        client.close()
        return

    if not dc.validate_request(req_raw):
        client.close()
        return

    req = dc.Request(
        req_raw.id,
        req_raw.group,
        req_raw.type,
        req_raw.command,
        req_raw.args,
    )

    try:
        result = command.run(req)

        if result is None:
            return

        response(client, req)
    except Exception as ex:
        message = f"Exception: {ex}"
        logging.error(message)

        # TODO: try to send error response back to client
        ...

        return


def set_logger(stream, level):
    logging.basicConfig(
        stream=stream,
        level=level,
        format="[%(asctime)s] [%(levelname)s] [%(filename)s] [%(module)s] [%(funcName)s] %(message)s",  # noqa: E501
    )


def main():
    set_logger(c.LOGGING_STREAM, c.LOGGING_LEVEL)

    logging.info(f"Server starts on port {c.PORT}")
    server.callbacks.ondata = ondata
    server.start(c.HOST, c.PORT)


if __name__ == "__main__":
    main()
