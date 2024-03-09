import logging
import select
import socket
import time

import config
import dc
import gp
import wifi

from . import callbacks, handler, utils

__all__ = [
    "callbacks",
    "handler",
    "utils",
    "start",
    "event_sockets",
]

event_sockets: list[socket.socket] = []


def start(host: str, port: int = 0):
    server_socket = socket.socket()

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    main_loop(server_socket)


def main_loop(server_socket: socket.socket):
    readable_sockets: list[socket.socket] = []

    while True:
        check_wifi()
        check_motion()

        if readable_sockets.__len__() == 0:
            readable_sockets.append(server_socket)

        try:
            readable, writable, errored = select.select(
                readable_sockets,
                [],
                [],
                config.SOCKET_TIMEOUT_SELECT,
            )
        except Exception as ex:
            logging.error(f'Got an exception while running select.select: "{ex}"')  # noqa: E501

            # Remove dead sockets
            for s in readable_sockets.copy():
                logging.debug(f"Remove socket {s} from readable_sockets")

                if s.fileno() == -1:
                    readable_sockets.remove(s)

            continue

        if (
            readable.__len__() == 0
            and writable.__len__() == 0
            and errored.__len__() == 0
        ):
            continue

        readable_sockets = handler.readable(server_socket, readable)

        if writable.__len__() > 0:
            logging.debug(f"There are writable sockets ({writable.__len__()})")

        handler.errored(errored)


def check_wifi() -> None:
    if not wifi.check():
        # TODO: Turn of the picow status led

        try:
            logging.debug("Try to connect to wifi...")

            if wifi.connect():
                # TODO: Turn on the picow status led
                pass
            else:
                # TODO: Oops, wait some seconds and try again
                raise Exception("Oops, wifi connection failed!")

        except Exception as ex:
            # TODO: do a machine reset
            ...

            logging.debug(f'Exception while trying to connect to wifi: "{ex}"')

            time.sleep(5)


def check_motion() -> None:
    motion = gp.motion.check()

    if event_sockets.__len__() == 0 or not motion:
        return

    closed: list[socket.socket] = []
    for s in event_sockets:
        utils.response(s, dc.Response(config.RESPONSE_MOTION_ID, None, motion))
        if s.fileno() == -1:
            closed.append(s)

    for s in closed:
        event_sockets.remove(s)
