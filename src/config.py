import logging
import sys

__all__ = [
    "HOST",
    "PORT",
    "LOGGING_STREAM",
    "LOGGING_LEVEL",
    "END_BYTE",
    "SOCKET_TIMEOUT_SELECT",
    "SOCKET_TIMEOUT_SEND",
]

HOST = "0.0.0.0"
PORT = 3000

LOGGING_STREAM = sys.stderr
LOGGING_LEVEL = logging.DEBUG

END_BYTE = b"\n"

SOCKET_TIMEOUT_SELECT: int | float | None = 0.25
SOCKET_TIMEOUT_SEND: int | float | None = 0.5
