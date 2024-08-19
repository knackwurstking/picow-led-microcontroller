import socket
from typing import Callable


ondata: Callable[[socket.socket, bytes], None] | None = None
