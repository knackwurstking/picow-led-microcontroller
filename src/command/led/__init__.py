from ..response import Response

__all__ = ["run_setter", "run_getter"]


def run_setter(command: str, *args) -> Response: ...


def run_getter(command: str, *args) -> Response: ...
