from typing import Union

from ... import dc

__all__ = ["run_setter", "run_getter"]


def set_duty(duty_cycle: int, pin: int) -> None: ...


def get_duty(*pins: int) -> int | None: ...


def run_setter(id: int, command: str, *args) -> dc.Response: ...


def run_getter(id: int, command: str, *args) -> dc.Response: ...
