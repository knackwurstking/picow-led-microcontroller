import socket
from typing import Callable

__all__ = ["ondata"]

ondata: Callable[[socket.socket, list[bytes]], None] | None = None
