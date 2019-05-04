from microbit import *
pin0.write_digital(0)
pin1.write_digital(0)
pin2.write_digital(0)
sleep(1000)

while True:
    if button_a.get_presses():
        pin0.write_digital(0)
        pin1.write_digital(1)
        pin2.write_digital(1)
        sleep(500)
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(1)
        sleep(500)
    if button_b.get_presses():
        pin0.write_digital(1)
        pin1.write_digital(1)
        pin2.write_digital(0)
        sleep(500)
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(1)
        sleep(500)

