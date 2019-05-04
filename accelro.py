from microbit import *
import math
while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    acceleration = math.sqrt(x**2 + y**2 + z**2)
    print("acceleration :",acceleration)
    #print("X, Y, Z :", x, y, z)
    sleep(500)
