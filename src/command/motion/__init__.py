from ... import dc

__all__ = ["run_getter", "run_event"]


def get_last_motion() -> int: ...


def event_watch_motions(host: str, port: int): ...


def run_getter(id: int, command: str, *args) -> dc.Response: ...


def run_event(id: int, command: str, *args) -> dc.Response: ...
