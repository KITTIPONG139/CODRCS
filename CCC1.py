from microbit import *
import radio
radio.on()
radio.config(channel = 19)
radio.config(power = 5)

message = "I love CS"



while True:
    if button_a.was_pressed():
        radio.send(Image.ARROW_NW)
    if button_b.was_pressed():
        radio.send(Image.HAPPY)
    sleep
    radio.send(message)
    incoming = radio.receive()
    if incoming is not None:

        display.show(incoming)
        print(incoming)
    sleep(500)

