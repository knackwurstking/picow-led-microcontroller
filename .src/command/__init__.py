from . import command


def run(request):
    return command.Command(
        request.id, request.group, request.type, request.command
    ).run(*request.args)
