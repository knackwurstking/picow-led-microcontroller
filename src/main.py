import logging
import socket

import command
import config as c
import server
from command.utils import ARGS_ERROR
from server.utils import response


def ondata(client: socket.socket, data: bytearray):
    logging.debug(f"client={client.getsockname()}, data={data}")

    if data.__len__() == 0:
        return

    try:
        result = command.run(int(data[0]), data[1:])
    except Exception as ex:
        if ex.__str__() == ARGS_ERROR.__str__() and type(ex) is type(
            ARGS_ERROR
        ):  # noqa: E501
            logging.debug(f'Invalid args for command: "{hex(data[0])}"')
            client.close()
            return

        logging.warning(f'Exception: "{data[0]}": {ex}')
        return

    if result is None:
        return

    response(client, data)


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
