from ..response import Response

__all__ = ["run_setter", "run_getter"]


def run_setter(id: int, command: str, *args) -> Response: ...


def run_getter(id: int, command: str, *args) -> Response: ...
