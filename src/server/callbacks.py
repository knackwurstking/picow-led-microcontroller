from typing import Callable

import socket

__all__ = ["ondata"]

ondata: Callable[[socket.socket, list[bytes]], bool] | None = None
