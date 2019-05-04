from microbit import *
compass.calibrate()

c1 = Image("00500:"
           "00500:"
           "00900:"
           "00000:"
           "00000")

c2 = Image("00050:"
           "00500:"
           "00900:"
           "00000:"
           "00000")

c3 = Image("00005:"
           "00050:"
           "00900:"
           "00000:"
           "00000")

c4 = Image("00000:"
           "00055:"
           "00900:"
           "00000:"
           "00000")

c5 = Image("00000:"
           "00000:"
           "00955:"
           "00000:"
           "00000")

c6 = Image("00000:"
           "00000:"
           "00950:"
           "00005:"
           "00000")

c7 = Image("00000:"
           "00000:"
           "00900:"
           "00050:"
           "00005")

c8 = Image("00000:"
           "00000:"
           "00900:"
           "00050:"
           "00050")

c9 = Image("00000:"
           "00000:"
           "00900:"
           "00500:"
           "00500")

c10 = Image("00000:"
            "00000:"
            "00900:"
            "00500:"
            "05000")

c11 = Image("00000:"
            "00000:"
            "00900:"
            "05000:"
            "50000")

c12 = Image("00000:"
            "00000:"
            "00900:"
            "55000:"
            "00000")

c13 = Image("00000:"
            "00000:"
            "55900:"
            "00000:"
            "00000")

c14 = Image("00000:"
            "50000:"
            "05900:"
            "00000:"
            "00000")

c15 = Image("50000:"
            "05000:"
            "00900:"
            "00000:"
            "00000")

c16 = Image("05000:"
            "05000:"
            "00900:"
            "00000:"
            "00000")

all_pin = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]

while True:
    sleep(100)
    b = compass.heading()
    needle = ((15 - compass.heading()) // 24) % 16
    print("needle: " , needle)
    print("bearing: " , b)
    display.show(all_pin[needle])