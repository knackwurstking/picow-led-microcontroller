import json
from sys import stderr

from constants import U16_MAX

from machine import PWM, Pin


class Cache:
    def __init__(self, name):
        self.name = name  # NOTE: "gpio"

    def read(self) -> None | object:
        if not self.name:
            return None

        try:
            file_name = self.get_file_name()
            with open(file_name, "r") as file:
                return json.load(file)
        except Exception:
            return None

    def write(self, data) -> None:
        if not self.name:
            return None

        try:
            file_name = self.get_file_name()
            with open(file_name, "w") as file:
                json.dump(data, file)
        except Exception:
            pass

        return None

    def get_file_name(self) -> str:
        return f"cache-{self.name}.json"


class GPIO:
    def __init__(self):
        self.cache = Cache("gpio")
        self.data = {
            "pins": [],
            "range": {
                "min": 0,
                "max": 255,
            },
        }

        data = self.cache.read()
        if isinstance(data, dict):
            self.data = data

        self._pins = []
        self._duty = []
        self.setup()

    def setup(self) -> None:
        self._pins = []
        self._duty = []

        for p in self.data["pins"]:
            p = PWM(Pin(p, value=1))
            p.freq(1000)
            self._pins.append(p)
            self._duty.append(self.data["range"]["min"])

        self.set_duty(*self._duty)

    def set_pins(self, *pins: int) -> None:
        self.data["pins"] = list(pins)
        self.cache.write(self.data)
        self.setup()

    def get_pins(self) -> list[int]:
        return self.data["pins"]

    def set_range(self, min: int, max: int) -> None:
        self.data["range"]["min"] = min
        self.data["range"]["max"] = max
        self.cache.write(self.data)

    def get_range(self) -> tuple[int, int]:
        return (self.data["range"]["min"], self.data["range"]["max"])

    def set_duty(self, *duty: int) -> None:
        self._duty = []

        for i, p in enumerate(self._pins):
            if len(duty) < i + 1:
                value =  int((1 - (self.data["range"]["min"] / self.data["range"]["max"])) * U16_MAX)
                print(f"[DEBUG] Set pin {p} to duty {value} [duty: {self.data["range"]["min"]}, range (max):{self.data["range"]["max"]}]", file=stderr)
                p.duty_u16(value)
                self._duty.append(self.data["range"]["min"])
            else:
                value =  int((1 - (duty[i] / self.data["range"]["max"])) * U16_MAX)
                print(f"[DEBUG] Set pin {p} to duty {value} [duty: {duty[i]}, range (max):{self.data["range"]["max"]}]", file=stderr)
                p.duty_u16(value)
                self._duty.append(duty[i])

    def get_duty(self) -> list[int]:
        return self._duty


gpio = GPIO()
