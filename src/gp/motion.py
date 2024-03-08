from __future__ import annotations

import socket
from typing import Callable

import config

__all__ = [
    "onchange",
    "GpMotion",
]

onchange: Callable[[int], None] | None = None


class Watcher:
    _host: str
    _port: int
    _client: socket.socket | None

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._client = None

    def start(self) -> Watcher:
        # TODO: try connecting to client and store client socket in `self.client`
        ...

        return self

    def stop(self) -> Watcher:
        ...

        return self

    def get_client(self) -> socket.socket | None:
        return self._client


class GpMotion:
    _pin: int  # NOTE: use -1 to unset pin
    _motion_timeout: int  # NOTE: resets the timer

    def __init__(
        self, pin: int = config.MOTION_PIN, motion_timeout: int = config.MOTION_TIMEOUT
    ) -> None:
        self._pin = pin
        self._motion_timeout = motion_timeout

    def set_pin(self, pin: int) -> GpMotion:
        """Set the motion sensor Gp Pin, disable with -1"""
        # TODO: update local config (save to pico)
        self._pin = pin
        return self

    def get_pin(self) -> int:
        """Returns the current motion sensor pin in use (-1 means its disabled)"""
        return self._pin

    def set_motion_timeout(self, value: int) -> GpMotion:
        # TODO: update local config (save to pico)
        self._motion_timeout = value
        return self

    def get_motion_timeout(self) -> int:
        return self._motion_timeout

    def get_last_motion(self) -> int: ...

    def watch(self, host: str, port: int) -> Watcher:
        return Watcher(host, port).start()
