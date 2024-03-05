from . import command

__all__ = [
    "run",
]


def run(id: int, group: str, type: str, command: str, *args) -> command.Response:
    return command.Command(id, group, type, command).run()
