from microbit import *

while True:
    a = pin0.read_analog()
    b = pin2.read_analog()

    b = int(4 * (b / 1023))
    sleep(50)
    print("x:" * str())