from microbit import *
import random

faces = [Image('00000:00000:00900:00000:00000:'),
        Image('00000:09000:00000:00090:00000'),
        Image('00000:09000:00900:00090:00000'),
        Image('00000:09090:00000:09090:00000'),
        Image('00000:09090:00900:09090:00000'),
        Image('00000:90909:00000:90909:00000')]

def RandomImages(n, delay):
    for i in range(0, n):
        display.show(random.choice(faces))
        sleep(delay)
        display.clear()
        sleep(delay)
while True:
    if button_a.was_pressed():
        RandomImages(20, 100)
        rolled = random.choice(faces)
        display.show(rolled)

    elif accelerometer.is_gesture("shake"):
        RandomImages(20, 100)
        rolled = random.choice(faces)
        display.show(rolled)