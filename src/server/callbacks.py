import socket
from typing import Callable

from .. import dc

__all__ = ["ondata"]

ondata: Callable[[socket.socket, bytearray], None] | None = None
