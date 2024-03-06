import logging
import socket

import command
import config as c
import server
from server.utils import response


def ondata(client: socket.socket, data: bytearray):
    logging.debug(f"client={client.getsockname()}, data={data}")

    if data.__len__() == 0:
        return

    try:
        result = command.run(int(data[0]), data[1:])

        if result is None:
            return

        response(client, data)
    except Exception as ex:
        message = f'Exception: "{data[0]}": {ex}'
        logging.error(message)

        # TODO: Send error response back to client?
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
