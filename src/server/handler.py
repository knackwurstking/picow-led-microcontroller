import logging
import socket

from . import utils

__all__ = ["readable", "writable", "errored"]


def readable(
    server: socket.socket, sockets: list[socket.socket]
) -> list[socket.socket]:
    logging.debug(f"server={server.getsockname()} sockets={sockets.__len__()}")

    clients: list[socket.socket] = []

    for s in sockets:
        if s is server:
            logging.debug("Waiting for client accept...")

            client, addr = s.accept()
            clients.append(client)

            logging.debug(f"Connected client from {addr}")
        else:
            data = utils.read_from_client(s)

            if s.fileno() == -1:
                continue

            utils.handle_client_data(s, data)

            # NOTE: append socket to clients if not closed
            if s.fileno() != -1:
                clients.append(s)

    return clients


def writable(sockets: list[socket.socket]) -> list[socket.socket]:
    logging.debug(f"sockets={sockets.__len__()}")

    clients: list[socket.socket] = []

    for s in sockets:
        logging.debug(f"Socket writable s={s}")
        s.close()

    return clients


def errored(sockets: list[socket.socket]) -> list[socket.socket]:
    logging.debug(f"sockets={sockets.__len__()}")

    clients: list[socket.socket] = []

    for s in sockets:
        logging.debug(f"Socket error: s={s}")
        s.close()

    return clients
