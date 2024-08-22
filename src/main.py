from socket import socket, SOL_SOCKET, SO_REUSEADDR
from time import sleep
from sys import stderr
import json

import machine
import network

from secrets import PASS, SSID
from constants import HOST, PORT, END_BYTE
from commands import COMMANDS


def main():
    setup()

    server = socket()
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)

    try:
        while True:
            print(f'[INFO] Waiting for client on "{HOST}:{PORT}"', file=stderr)
            client, address = server.accept()
            print(f'[INFO] Connected client from "{address}"', file=stderr)

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
                continue

            try:
                data = json.loads(data.strip())
            except Exception as ex:
                print(f"[WARN] Convert data to JSON failed: {ex}", file=stderr)
                client.close()
                continue

            try:
                request = {
                    "id": data.get("id", 0),
                    "group": data["group"],
                    "type": data["type"],
                    "command": data["command"],
                    "args": data.get("args", []),
                }

                try:
                    run(client, request)
                except Exception as ex:
                    print(f"[WARN] run failed: {ex}", file=stderr)
                    client.close()
                    continue

            except Exception as ex:
                print(f"[WARN] Invalid client request: {ex}", file=stderr)
                client.close()
                continue

    finally:
        disable_led()


def setup():
    disable_led()

    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        sta_if.active(True)

        print("[DEBUG] Try to connect...", file=stderr)
        sta_if.connect(SSID, PASS)

        while not sta_if.isconnected():
            print("[DEBUG] ...wait for connection...", file=stderr)
            sleep(0.25)

        enable_led()

    print(f"[DEBUG] ...ifconfig={sta_if.ifconfig()}", file=stderr)


def run(client, request):
    response_data = COMMANDS[request["group"]][request["type"]][request["command"]](
        *request["args"]
    )

    # TODO: Send response to client (if id is not -1)
    ...


def enable_led():
    led = machine.Pin("LED", machine.Pin.OUT)
    led.on()


def disable_led():
    led = machine.Pin("LED", machine.Pin.OUT)
    led.off()


if __name__ == "__main__":
    main()
