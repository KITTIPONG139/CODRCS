from microbit import *
while True:
    if button_a.was_pressed():
        display.scroll("TONG")
    else:
        display.show(Image.HAPPY)
    sleep(1000)