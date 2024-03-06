from typing import Union

from ..response import Response

__all__ = ["run_setter", "run_getter"]


def set_duty(duty_cycle: int, pin: Union[None, int] = None) -> None: ...


def get_duty(*pins: int) -> int | None: ...


def run_setter(id: int, command: str, *args) -> Response: ...


def run_getter(id: int, command: str, *args) -> Response: ...
