import network
from sys import stderr

from . import secrets


def do_connect():
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print("[INFO] connecting to network...", file=stderr)

        sta_if.active(True)
        sta_if.connect(secrets.SSID, secrets.PASS)

        while not sta_if.isconnected():
            pass

    print("network config:", sta_if.ipconfig("addr4"))
