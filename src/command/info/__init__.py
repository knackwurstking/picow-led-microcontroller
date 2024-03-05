from ..response import Response

__all__ = ["run_getter"]


def get_temp() -> float: ...


def get_disk_usage() -> dict[str, int]: ...


def get_version() -> str: ...


def run_getter(id: int, command: str, *args) -> Response: ...
