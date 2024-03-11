import logging
from dataclasses import dataclass
from typing import Any, Union

__all__ = ["Response", "Request", "validate_request"]


@dataclass
class Response:
    id: int
    error: str | None
    data: Any


@dataclass
class Request:
    id: int
    group: str
    type: str
    command: str
    args: list[Union[int, float, str]]


def validate_request(req: Any) -> bool:
    try:
        if not isinstance(req.get("id", 0), int):
            return False

        if not isinstance(req["group"], str):
            return False

        if not isinstance(req["type"], str):
            return False

        if not isinstance(req["command"], str):
            return False

        if not isinstance(req.get("args", []), list):
            return False

        for arg in req.get("args", []):
            if (
                not isinstance(arg, int)
                and not isinstance(arg, float)
                and not isinstance(arg, str)
            ):
                return False
    except Exception as ex:
        logging.warn(f"Exception while validate request data: {ex}")
        return False

    return True
