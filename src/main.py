import json
from socket import SO_REUSEADDR, SOL_SOCKET, socket
from sys import stderr
from time import sleep

import machine
import network

from commands import COMMANDS
from constants import END_BYTE, HOST, PORT
from secrets import PASS, SSID


def main():
    setup()

    server = socket()
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)

    try:
        while True:
            print(
                f'[INFO ] Waiting for client on "{HOST}:{PORT}"',
                file=stderr,
            )
            client, address = server.accept()
            print(f'[INFO ] Connected client from "{address}"', file=stderr)

            try:
                handleClient(client)
            except Exception as e:
                print(f"[WARN ] Handle client exception: {str(e)}")
                client.close()

    finally:
        disable_led()


def setup():
    disable_led()

    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        sta_if.active(True)

        print("[DEBUG] Try to connect...", file=stderr)
        sta_if.connect(SSID, PASS)

        retry_count = 0
        while not sta_if.isconnected():
            if retry_count > 20:
                print("[ERROR] Connection failed, retry...")
                return setup()

            retry_count += 1

            print("[DEBUG] ...wait for connection...", file=stderr)
            sleep(0.5)

    enable_led()
    print(f"[DEBUG] ...ifconfig={sta_if.ifconfig()}", file=stderr)


def handleClient(client):
    while True:
        data = bytes()
        while True:
            chunk = client.recv(1)
            if chunk == END_BYTE:
                break

            if chunk:
                data += chunk
            else:
                break

        if len(data) == 0:
            client.close()
            return

        try:
            data = json.loads(data.strip())

        except Exception as ex:
            print(f"[WARN ] Convert data to JSON failed: {ex}", file=stderr)
            client.close()
            return

        try:
            request = {
                "id": data.get("id", 0),
                "group": data["group"],
                "type": data["type"],
                "command": data["command"],
                "args": data.get("args", []),
            }

            try:
                print(
                    f"[DEBUG] Run requested command: {request['group']} "
                    + f"{ request['type'] } {request['command']} "
                    + f"{request['args']}"
                )
                run(client, request)

            except Exception as ex:
                print(f"[ERROR] run failed: {ex}", file=stderr)
                client.close()
                return

        except Exception as ex:
            print(f"[WARN ] Invalid client request: {ex}", file=stderr)
            client.close()
            return


def run(client, request):
    response = {
        "id": request["id"],
        "error": None,
        "data": None,
    }

    try:
        if request["group"] not in COMMANDS:
            response["error"] = f'command group "{request["group"]}" not found'

        if request["type"] not in COMMANDS[request["group"]]:
            response["error"] = f'command type "{request["type"]}" not found'

        if request["command"] not in COMMANDS[request["group"]][request["type"]]:
            response["error"] = f'command "{request["command"]}" not found'

        if response["error"] is None:
            response["data"] = COMMANDS[request["group"]][request["type"]][
                request["command"]
            ](*request["args"])

    except AssertionError:
        message = "wrong args"
        print("[ERROR] " + message)
        response["error"] = message

    except Exception as e:
        message = f"command failed to run: {str(e)} (type: {type(e).__name__})"
        print("[ERROR] " + message + ": " + str(e))
        response["error"] = message

    if response["id"] != -1:
        data = json.dumps(response)
        client.settimeout(0.5)
        client.send(data.encode() + END_BYTE)
        client.settimeout(None)


def enable_led():
    led = machine.Pin("LED", machine.Pin.OUT)
    led.on()


def disable_led():
    led = machine.Pin("LED", machine.Pin.OUT)
    led.off()


if __name__ == "__main__":
    main()
