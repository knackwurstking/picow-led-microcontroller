import sys

VERSION = "0.0.1"

HOST = "0.0.0.0"
PORT = 3000

LOGGING_STREAM = sys.stderr

END_BYTE = "\n".encode()

SOCKET_TIMEOUT_SELECT: int | float | None = 0.25
SOCKET_TIMEOUT_SEND: int | float | None = 0.5

# color pins in order (ex.: [r, g, b, w])
COLOR_PINS: list[int] = []

LED_PWM_RANGE_MIN: int = 0
LED_PWM_RANGE_MAX: int = 100

ID_DEFAULT = 0
ID_DISABLED = -1  # Disabled response
