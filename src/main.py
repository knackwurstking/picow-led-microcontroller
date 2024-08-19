from typing import Any
import json
import logging
import socket

import command
import config as c
import dc
import server


def ondata(client: socket.socket, data: bytes):
    logging.debug(f"client={client.getsockname()}, data={data!r}")

    req_raw: Any = None

    try:
        req_raw = json.loads(data.strip())
    except Exception as ex:
        logging.debug(f"Exception while parsing json data: {ex}")
        client.close()
        return

    if not dc.validate_request(req_raw):
        logging.debug(f"Invalid request: {req_raw}")
        client.close()
        return

    req = dc.Request(
        req_raw.get("id", 0),
        req_raw["group"],
        req_raw["type"],
        req_raw["command"],
        req_raw.get("args", []),
    )

    try:
        result = command.run(client, req)

        if result is None:
            return

        if req.id != c.ID_DISABLED:
            server.utils.response(client, result)
    except Exception as ex:
        message = f"exception: {ex}"
        logging.error(message)

        if req.id != -1:
            server.utils.response(client, dc.Response(req.id, message, None))
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
