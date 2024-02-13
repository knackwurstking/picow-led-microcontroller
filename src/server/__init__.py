import select
import socket

_readable_sockets = []


def start():
    # TODO: needed callbacks:
    #   "ondata(s: socket, data: bytearray)"

    server_socket = socket.socket()
    _readable_sockets.append(server_socket)
    _start_main_loop(server_socket)


def _start_main_loop(server_socket: socket.socket):
    while True:
        readable, __writable__, __errored__ = select.select(
            _readable_sockets, [], [], 0
        )  # TODO: maybe find a better timeout value?

        _handle_readable(server_socket, readable)

        # TODO: check errored sockets


def _handle_readable(server_socket: socket.socket, readable: list[socket.socket]):
    for sock in readable:
        if sock is server_socket:
            client, __addr__ = server_socket.accept()
            _readable_sockets.append(client)
        else:
            data = _read_from_client(sock)
            _handle_client_data(data)


def _read_from_client(client: socket.socket) -> list[bytes]:
    data: list[bytes] = []

    while True:
        chunk = client.recv(1)
        if chunk:
            data.append(chunk)
        else:
            break

    return data


def _handle_client_data(data: list[bytes]):
    if data.__len__() == 0:
        return

    # TODO: if data run callback "ondata"
    # ondata(sock, data)
