from . import dc

__all__ = [
    "run",
]


def run(id: int, group: str, type: str, command: str, *args) -> dc.Response:
    return dc.Command(id, group, type, command).run()
