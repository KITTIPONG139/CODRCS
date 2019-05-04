from microbit import *
import radio

radio.on()
radio.config(channel = 19)
radio.config(power = 7)

while True:
    if button_a.was_pressed():
        radio.send(Image.FABULOUS)
    if button_b.was_pressed():
        radio.send(Image.HAPPY)
    sleep(100)
-------------------------------------------
from microbit import *
import radio

radio.on()
radio.config(channel = 19)

while True:
    s = radio.receive()
    if s is not None:
        print(s)
        i = Image(s)
        display.show(i)
------------------------------
if button_a.was_pressed():
    radio.send("H")

------------------------------
s = radio.receive()
if s is not None:
    if s == "H":
        display.show(Image.FABULOUS)