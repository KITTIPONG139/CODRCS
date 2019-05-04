from microbit import *
compass.calibrate()#calibrate การทำให้มันเทียงตรงก่อน หรือแม่นก่อน
while True:
    bearing = compass.heading()
    print(bearing)
    sleep(100)