import socket

from . import command


def run(client: socket.socket, request):
    return command.Command(
        request.id, request.group, request.type, request.command
    ).run(client, *request.args)
