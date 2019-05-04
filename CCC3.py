from microbit import *
import radio

radio.on()
radio.config(channel = 19)
radio.config(power = 7)

while True:
    s = radio.receive()
    if s is not None:
        if s == (Image.FABULOUS):
            display.show(Image.ANGRY)
        if s == (Image.CLOCK9)