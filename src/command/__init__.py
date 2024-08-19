import socket

import dc

from . import command


def run(client: socket.socket, req: dc.Request) -> dc.Response:
    return command.Command(req.id, req.group, req.type, req.command).run(
        client, *req.args
    )
