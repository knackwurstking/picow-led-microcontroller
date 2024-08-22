import json

from machine import PWM, Pin


class Cache:
    def __init__(self, name):
        self.name = name  # NOTE: "gpio"

    def read(self) -> None | object:
        if not self.name:
            return None

        try:
            file_name = self.get_file_name()
            with open(file_name) as file:
                return json.load(file)
        except Exception:
            return None

    def write(self, data) -> None:
        if not self.name:
            return None

        try:
            file_name = self.get_file_name()
            with open(file_name) as file:
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
                "max": 100,
            },
        }

        data = self.cache.read()
        if isinstance(data, dict):
            self.data = data

        self.pins = []
        self.setup()

    def setup(self) -> None:
        self.pins = []
        for p in self.data["pins"]:
            p = PWM(Pin(p, value=1), freq=100)
            p.set_duty_cycle(self.data["range"]["min"])
            self.pins.append(p)

    def set_pins(self, *pins) -> None:
        self.data["pins"] = list(pins)
        self.cache.write(self.data)
        self.setup()

    def get_pins(self) -> list[int]:
        return self.data["pins"]

    def set_range(self, min, max) -> None:
        self.data["range"]["min"] = min
        self.data["range"]["max"] = max
        self.cache.write(self.data)

    def get_range(self) -> tuple[int, int]:
        return (self.data["range"]["min"], self.data["range"]["max"])

    def set_duty(self, *args): ...

    def get_duty(self): ...


gpio = GPIO()
