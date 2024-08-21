import os

import config
import dc
# from picozero import pico_temp_sensor  # type: ignore


def get_temp() -> float:
    # return pico_temp_sensor.temp
    return 23.35  # TODO: testing


def get_disk_usage() -> dict[str, int]:
    disk = os.statvfs("/")

    block_size = disk[0]
    total_blocks = disk[2]
    free_blocks = disk[3]

    used = (block_size * total_blocks) - (block_size * free_blocks)
    free = block_size * free_blocks

    return {
        "used": used,
        "free": free,
    }


def get_version() -> str:
    return config.VERSION


def run(id: int, _type: str, command: str, *args):
    response = dc.new_response(id)
    run_command = None

    if _type == "get":
        try:
            run_command = get_getter_command(command)
        except Exception as ex:
            response["error"] = str(ex)
    else:
        response["error"] = f'"{_type}" command "{command}" not found!'

    if run_command is None:
        return response

    try:
        response["data"] = run_command(*args)
    except Exception as ex:
        response["error"] = str(ex)

    return response


def get_getter_command(command: str):
    run_command = None

    if command == "temp":
        run_command = get_temp
    elif command == "disk-usage":
        run_command = get_disk_usage
    elif command == "version":
        run_command = get_version
    else:
        raise Exception(f'command "{command}" not found!')

    return run_command
