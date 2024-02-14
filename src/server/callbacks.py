import socket
from typing import Callable

__all__ = ["ondata"]

ondata: Callable[[socket.socket, list[bytes]], bool] | None = None
