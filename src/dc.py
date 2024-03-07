from typing import Union
from dataclasses import dataclass

__all__ = ["Response", "Request", "validate_request"]


@dataclass
class Response:
    id: int
    error: str | None
    data: any


@dataclass
class Request:
    id: int
    group: str
    type: str
    command: str
    args: list[Union[int, float, str]]


def validate_request(req: any) -> bool:
    if not isinstance(req.id, int):
        return False

    if not isinstance(req.group, str):
        return False

    if not isinstance(req.type, str):
        return False

    if not isinstance(req.command, str):
        return False

    if not isinstance(req.args, list):
        return False

    for arg in req.args:
        if (
            not isinstance(arg, int)
            and not isinstance(arg, float)
            and not isinstance(arg, str)
        ):
            return False

    return True
