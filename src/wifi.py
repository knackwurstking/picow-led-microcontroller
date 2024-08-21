from sys import stderr
import time

import machine
import network

import secrets


def do_connect():
    disable_led()
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        sta_if.active(True)

        print("[DEBUG] Try to connect...", file=stderr)
        sta_if.connect(secrets.SSID, secrets.PASS)

        while not sta_if.isconnected():
            print("[DEBUG] ...wait for connection...", file=stderr)
            time.sleep(0.25)

        enable_led()

    print(f"[DEBUG] ...ifconfig={sta_if.ifconfig()}", file=stderr)


def enable_led():
    led = machine.Pin("LED", machine.Pin.OUT)
    led.on()


def disable_led():
    led = machine.Pin("LED", machine.Pin.OUT)
    led.off()
