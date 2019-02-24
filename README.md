from microbit import *
import radio

radio.on()
radio.config(channel = 19)
radio.config(power = 7)

while True:
    y = accelerometer.get_y()
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    if a and y < -300:
        display.show(Image.ARROW_NW)
        radio.send("NW")
    if a and y > 300:
         display.show(Image.ARROW_SW)
         radio.send("SW")
    if b and y < -300:
         display.show(Image.ARROW_NE)
         radio.send("NE")
    if b and y > 300:
         display.show(Image.ARROW_SE)
         radio.send("SE")
    if y > 300:
        display.show(Image.ARROW_S)
        radio.send("S")
    if y < -300:
        display.show(Image.ARROW_N)
        radio.send("N")
