from ..response import Response

__all__ = ["run_getter", "run_event"]


def run_getter(id: int, command: str, *args) -> Response: ...


def run_event(id: int, command: str, *args) -> Response: ...
