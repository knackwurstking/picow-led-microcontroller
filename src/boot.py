import secrets

import machine
import network


def do_connect():
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(secrets.SSID, secrets.PASS)

        while not sta_if.isconnected():
            pass

        enable_led()


def enable_led():
    led = machine.Pin("LED", machine.Pin.OUT)
    led.on()
