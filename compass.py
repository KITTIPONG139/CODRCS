from microbit import *
compass.calibrate()
#เข็มทิศ
while True:
    needle = ((15-compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needlex])

#+ add
#- substract
#* multiple
#/ divide
#% Modulus
#// floor division
#** Exponent