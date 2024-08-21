import json
import socket
from sys import stderr

import command
import config as c
import dc
import server


def ondata(client: socket.socket, data: bytes):
    print(f"[DEBUG] client={client.getsockname()}, data={data!r}", file=stderr)

    req_raw = None

    try:
        req_raw = json.loads(data.strip())
    except Exception as ex:
        print(f"[DEBUG] Exception while parsing json data: {ex}", file=stderr)
        client.close()
        return

    if not dc.validate_request(req_raw):
        print(f"[DEBUG] Invalid request: {req_raw}", file=stderr)
        client.close()
        return

    try:
        request = dc.new_request(
            req_raw.get("id", 0),
            req_raw["group"],
            req_raw["type"],
            req_raw["command"],
            req_raw.get("args", []),
        )
    except AssertionError:
        return

    try:
        result = command.run(client, request)

        if result is None:
            return

        if request["id"] != c.ID_DISABLED:
            server.utils.response(client, result)
    except Exception as ex:
        message = f"exception: {ex}"
        print("[ERROR] " + message, file=stderr)

        if request["id"] != -1:
            server.utils.response(
                client,
                dc.new_response(request["id"], error=message),
            )

        return


def main():
    print(f"[INFO] Server starts on port {c.PORT}", file=stderr)
    server.callbacks.ondata = ondata
    server.start(c.HOST, c.PORT)


if __name__ == "__main__":
    main()
