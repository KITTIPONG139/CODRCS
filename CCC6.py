from microbit import *

while True:
    a = pin2.read_analog()
    a = int(100 * (a/102))
    sleep(50)
    print("a:" + str(a))
    pin0.write_analog(a)
    sleep(10)