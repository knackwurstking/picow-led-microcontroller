import os

from gpio import gpio
from picozero import pico_temp_sensor

from constants import VERSION


def config_set_pins(*args) -> None:
    pins = []
    for arg in list(args):
        pins.append(int(arg))

    gpio.set_pins(*pins)

    return None


def config_get_pins(*args) -> list[int]:
    return gpio.get_pins()


def info_get_temp(*args) -> float | None:
    return pico_temp_sensor.temp


def info_get_disk_usage(*args) -> dict:
    disk = os.statvfs("/")

    block_size = disk[0]
    total_blocks = disk[2]
    free_blocks = disk[3]

    used = (block_size * total_blocks) - (block_size * free_blocks)
    free = block_size * free_blocks

    return {"used": used, "free": free}


def info_get_version(*args) -> str:
    return VERSION


def led_set_color(*args) -> None:
    duty = []
    for arg in list(args):
        duty.append(int(arg))

    gpio.set_duty(*duty)


def led_get_color(*args) -> list[int]:
    return gpio.get_duty()


# NOTE: each command takes `*args` as parameter and
#       returns the client response data
COMMANDS = {
    "config": {
        "set": {
            "pins": config_set_pins,
        },
        "get": {
            "pins": config_get_pins,
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
            "color": led_set_color,
        },
        "get": {
            "color": led_get_color,
        },
    },
}
