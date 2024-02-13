import sys
import socket

import server


def ondata(client: socket.socket, data: list[bytes]):
    # TODO: handle client data and send a response or just close and exit
    print(f"ondata: client={client.getsockname()}, data={data}", file=sys.stderr)

    return True


if __name__ == "__main__":
    server.callbacks.ondata = ondata
    server.start("0.0.0.0", 3000)
