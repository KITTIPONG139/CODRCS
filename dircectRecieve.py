from microbit import *
import radio

radio.on()
radio.config(channel = 19)

while True:
    s = radio.receive()
    if s is not None:
        if s == "N":
            display.show(Image.ARROW_N)
        elif s == "S":
            display.show(Image.ARROW_S)
        elif s == "NE":
            display.show(Image.ARROW_NE)
        elif s == "NW":
            display.show(Image.ARROW_NW)
        elif s == "SE":
            display.show(Image.ARROW_SE)
        elif s == "SW":
            display.show(Image.ARROW_SW)
    sleep(20)