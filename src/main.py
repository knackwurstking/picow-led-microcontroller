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
            handleClient(client)

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
            print(f"[WARN] Convert data to JSON failed: {ex}", file=stderr)
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
                print(f"[DEBUG] group={request["group"]}, type={
                    request["type"]}, command={request["command"]}")
                run(client, request)

            except Exception as ex:
                print(f"[ERROR] run failed: {ex}", file=stderr)
                client.close()
                return

        except Exception as ex:
            print(f"[WARN] Invalid client request: {ex}", file=stderr)
            client.close()
            return


def run(client, request):
    response = {
        "id": request["id"],
        "error": None,
        "data": None,
    }

    try:
        response["data"] = COMMANDS[request["group"]][request["type"]][
            request["command"]
        ](*request["args"])

    except Exception as ex:
        print(f"[ERROR] run command failed: {ex}")
        response["error"] = ex

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
