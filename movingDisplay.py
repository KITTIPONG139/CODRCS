from microbit import *
im = Image('99000:99000:99000:99000:99000:')
im = Image('09000:09000:00900:00000:90000:')

display.show(im)
while True:
    im = im.shift_up(2)
    display.show(im)
    sleep(500)
    im = im.shift_right(2)
    display.show(im)
    sleep(500)
    im = im.shift_down(1)
    display.show(im)
    sleep(500)
    im = im.shift_left(1)
    display.show(im)
    sleep(500)

