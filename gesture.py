from microbit import *

while True:
    if accelerometer.is_gesture("up"):
        display.show(Image.ARROW_S)
    elif accelerometer.is_gesture("right"):
        display.show(Image.ARROW_E)
    elif accelerometer.is_gesture("down"):
        display.show(Image.ARROW_N)
    elif accelerometer.is_gesture("left"):
        display.show(Image.ARROW_W)
        #display.show(Image.ANGRY)
    else:
        display.clear()
    sleep(20)

    #fup, down, left, right, fabs up, fabs down, freefall, 3g, 6g, 8g, shake
