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
