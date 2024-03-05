from dataclasses import dataclass

__all__ = ["Response"]


@dataclass
class Response:
    id: int
    error: str | None
    data: any
