from microbit import *
import math
compass.calibrate()
while True:
    x = compass.get_x()
    y = compass.get_y()
    angle = math.atan2(y, x) *180/math.pi
    print("x reading:", x, ",y reading:", y)
    print("Directon: ", angle)
    sleep(500)