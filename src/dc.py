import logging


def new_response(id, error=None, data=None):
    return {
        "id": id,
        "error": error,
        "data": data,
    }


def new_request(id, group, _type, command, args):
    assert isinstance(id, int)
    assert isinstance(group, str)
    assert isinstance(_type, str)
    assert isinstance(command, str)
    assert isinstance(args, list)

    return {
        "id": id,
        "group": group,
        "type": _type,
        "command": command,
        "args": args,
    }


def validate_request(req) -> bool:
    try:
        if not isinstance(req.get("id", 0), int):
            return False

        if not isinstance(req["group"], str):
            return False

        if not isinstance(req["type"], str):
            return False

        if not isinstance(req["command"], str):
            return False

        if not isinstance(req.get("args", []), list):
            return False

        for arg in req.get("args", []):
            if (
                not isinstance(arg, int)
                and not isinstance(arg, float)
                and not isinstance(arg, str)
            ):
                return False

    except Exception as ex:
        logging.warn(f"Exception while validate request data: {ex}")
        return False

    return True
