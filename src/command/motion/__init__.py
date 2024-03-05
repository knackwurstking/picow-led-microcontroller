from ..response import Response

__all__ = ["run_getter", "run_event"]


def run_getter(command: str, *args) -> Response: ...


def run_event(command: str, *args) -> Response: ...
