import select
import socket


def start():
    sock = socket.socket()
    r_list = [sock]

    while True:
        readable, __writable__, __errored__ = select.select(r_list, [], [], 0)

        for s in readable:
            if s is sock:
                client, __addr__ = sock.accept()
                r_list.append(client)
            else:
                # TODO: recv data from client
                ...

        # TODO: check errored sockets
