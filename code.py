import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import digitalio

btns = [
    {
        "name": 'a',
        "ref": board.D3,
        "key": Keycode.A,
        "pressed": False,
        "pointer": None
    },
    {
        "name": 'b',
        "ref": board.D4,
        "key": Keycode.B,
        "pressed": False,
        "pointer": None
    },
    {
        "name": None, # unused start button
        "ref": board.D5,
        "key": None,
        "pressed": False,
        "pointer": None
    },
    {
        "name": 'down',
        "ref": board.D6,
        "key": Keycode.DOWN_ARROW,
        "pressed": False,
        "pointer": None
    },
    {
        "name": 'right',
        "ref": board.D7,
        "key": Keycode.RIGHT_ARROW,
        "pressed": False,
        "pointer": None
    },
    {
        "name": 'up',
        "ref": board.D8,
        "key": Keycode.UP_ARROW,
        "pressed": False,
        "pointer": None
    },
    {
        "name": 'left',
        "ref": board.D9,
        "key": Keycode.LEFT_ARROW,
        "pressed": False,
        "pointer": None
    },
]

for btn in btns:
    btn["pointer"] = digitalio.DigitalInOut(btn["ref"])
    btn["pointer"].direction = digitalio.Direction.INPUT
    btn["pointer"].pull = digitalio.Pull.UP

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

while True:
    for btn in btns:
        if not btn["pointer"].value:
            # make sure we aren't already pressing this button
            if not btn["pressed"]:
                keyboard.press(btn["key"])
                btn["pressed"] = True

        # if we aren't pressing the button
        # but it was pressed last time
        # we reset
        elif btn["pressed"]:
            keyboard.release(btn["key"])
            btn["pressed"] = False

    time.sleep(0.05)
