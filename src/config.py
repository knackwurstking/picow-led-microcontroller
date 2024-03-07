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

# color pins in order (ex.: [r, g, b, w])
COLOR_PINS: list[int] = []

LED_PWM_RANGE_MIN: min = 0
LED_PWM_RANGE_MAX: min = 100

# motion pin set to -1 will disable the motion sensor
MOTION_PIN: int = -1
MOTION_TIMEOUT: int = 60000  # 60 seconds
