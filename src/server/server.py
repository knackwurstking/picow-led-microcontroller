import logging
import select
import socket
import time

import wifi

from . import handler

__all__ = [
    "start",
]


def start(host: str, port: int = 0):
    server_socket = socket.socket()

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    main_loop(server_socket)


def main_loop(server_socket: socket.socket):
    readable_sockets = []
    writable_sockets = []
    errored_sockets = []

    while True:
        check_wifi()

        if readable_sockets.__len__() == 0:
            readable_sockets.append(server_socket)

        try:
            readable, writable, errored = select.select(
                readable_sockets, writable_sockets, errored_sockets, 0.25
            )
        except Exception as ex:
            logging.error(
                f'Got an exception while running select.select: "{ex}"')

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
        writable_sockets = handler.writable(writable)
        errored_sockets = handler.errored(errored)


def check_wifi():
    if not wifi.check():
        # TODO: Turn of the picow status led

        try:
            logging.debug("Try to connect to wifi...")

            if wifi.connect():
                # TODO: Turn on the picow status led
                pass
            else:
                # TODO: Oooops, wait some seconds and try again
                raise Exception("Oooops, wifi connection failed!")

        except Exception as ex:
            # TODO: do a machine reset
            ...

            logging.debug(f'Exception wile trying to connect to wifi: "{ex}"')

            time.sleep(5)
