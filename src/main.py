import logging
import socket

import command
import config as c
import server
from command.utils import ARGS_ERROR
from server.utils import response


def ondata(client: socket.socket, data: list[bytes]):
    logging.debug(f"client={client.getsockname()}, data={data}")

    if data.__len__() == 0:
        return

    try:
        result = command.run(data[0], data[1:])
    except Exception as ex:
        if ex.__str__() == ARGS_ERROR.__str__() and type(ex) is type(
            ARGS_ERROR
        ):  # noqa: E501
            logging.debug(
                f"Exception while running command '{hex(data[0])}': {ex}"
            )  # noqa: E501
            client.close()
            return

        logging.warning(
            f"Exception while running command '{hex(data[0])}': {ex}"
        )  # noqa: E501
        return

    if result is None:
        return

    response(client, data)


if __name__ == "__main__":
    logging.basicConfig(
        stream=c.LOGGING_STREAM,
        level=c.LOGGING_LEVEL,
        format="[%(asctime)s] [%(levelname)s] [%(filename)s] [%(module)s] [%(funcName)s] %(message)s",  # noqa: E501
    )

    logging.info(f"Server starts on port {c.PORT}")
    server.callbacks.ondata = ondata
    server.start(c.HOST, c.PORT)
