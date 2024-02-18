import logging
import socket
import sys

import config as c

import server


def ondata(client: socket.socket, data: list[bytes]):
    logging.debug(f"[main.ondata] client={client.getsockname()}, data={data}")

    # TODO: run command...
    ...


if __name__ == "__main__":
    logging.basicConfig(
        stream=sys.stderr,
        level=c.LOGGING_LEVEL,
        format="[%(asctime)s] [%(levelname)s] [%(filename)s] [%(module)s] [%(funcName)s] %(message)s",
    )

    logging.info(f"Server starts on port {c.PORT}")
    server.callbacks.ondata = ondata
    server.start(c.HOST, c.PORT)
