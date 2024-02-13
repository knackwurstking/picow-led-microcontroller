import socket

import server


def on_data(client: socket.socket, data: list[bytes]):
    # TODO: handle client data and send a response or just close and exit

    client.close()
    return True


if __name__ == "__main__":
    server.ondata = on_data
    server.start()
