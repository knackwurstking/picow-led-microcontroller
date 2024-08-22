import json

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

        self._pins = []
        self._duty = []
        self.setup()

    def setup(self) -> None:
        self._pins = []
        self._duty = []

        for p in self.data["pins"]:
            p = PWM(Pin(p, value=1), freq=100)

            p.set_duty_cycle(self.data["range"]["min"])

            self._pins.append(p)
            self._duty.append(self.data["range"]["min"])

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
        for i, p in enumerate(self._pins):
            if len(duty) < i + 1:
                p.duty_u16(
                    int(
                        (1 - (self.data["range"]["min"] / self.data["range"]["max"]))
                        * U16_MAX
                    ),
                )

                self._duty.append(self.data["range"]["min"])
            else:
                p.duty_u16(
                    int((1 - (duty[i] / self.data["range"]["max"])) * U16_MAX),
                )

                self._duty.append(duty[i])

    def get_duty(self) -> list[int]:
        return self._duty


gpio = GPIO()
