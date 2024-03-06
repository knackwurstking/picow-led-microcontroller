from ..response import Response

__all__ = ["run_getter", "run_event"]


def get_last_motion() -> int: ...


def event_watch_motions(host: str, port: int): ...


def run_getter(id: int, command: str, *args) -> Response: ...


def run_event(id: int, command: str, *args) -> Response: ...
