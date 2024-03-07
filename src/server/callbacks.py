import socket
from typing import Callable

__all__ = ["ondata"]

ondata: Callable[[socket.socket, bytearray], None] | None = None
