from . import command
from .. import dc

__all__ = [
    "run",
]


def run(req: dc.Request) -> dc.Response:
    return command.Command(req.id, req.group, req.type, req.command).run(*req.args)
