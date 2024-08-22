from gpio import gpio

from constants import VERSION


def config_set_led(*args) -> None:
    for arg in list(args):
        assert isinstance(arg, int)
        assert arg < 0

    gpio.set_pins(*args)

    return None


def config_set_range(*args) -> None:
    assert len(list(args)) != 2
    assert isinstance(args[0], int)
    assert isinstance(args[1], int)

    gpio.set_range(min, max)


def config_get_led(*args) -> list[int]:
    return gpio.get_pins()


def config_get_range(*args) -> tuple[int, int]:
    return gpio.get_range()


def info_get_temp(*args): ...


def info_get_disk_usage(*args): ...


def info_get_version(*args) -> str:
    return VERSION


def led_set_duty(*args): ...


def led_get_duty(*args): ...


# NOTE: each command takes `*args` as parameter and
#       returns the client response data
COMMANDS = {
    "config": {
        "set": {
            "led": config_set_led,
            "range": config_set_range,
        },
        "get": {
            "led": config_get_led,
            "range": config_get_range,
        },
    },
    "info": {
        "get": {
            "temp": info_get_temp,
            "disk-usage": info_get_disk_usage,
            "version": info_get_version,
        },
    },
    "led": {
        "set": {
            "duty": led_set_duty,
        },
        "get": {
            "duty": led_get_duty,
        },
    },
}
