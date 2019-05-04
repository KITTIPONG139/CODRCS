from microbit import *
#กดปุ่ม
while True:
    if pin0.is_touched():
        display.set_pixel(0,0,9)
        boat1 = Image("09390:""93039:""90909:""93039:""09390:")
        boat2 = Image("05350:""53035:""50505:""53035:""05350:")
        boat3 = Image("02120:""21012:""20202:""21012:""02120:")
        boat4 = Image("01010:""10001:""10101:""10001:""01010:")
        boat5 = Image("00000:""00000:""00000:""00000:""00000:")
        boat7 = Image("01010:""10001:""10101:""10001:""01010:")
        boat8 = Image("02120:""21012:""20202:""21012:""02120:")
        boat9 = Image("05350:""53035:""50505:""53035:""05350:")
        boat10 = Image("09390:""93039:""90909:""93039:""09390:")
        boat11 = Image("00000:""93039:""90909:""93039:""09390:")
        boat12 = Image("00000:""00000:""90909:""93039:""09390:")
        boat13 = Image("00000:""00000:""00000:""93039:""09390:")
        boat14 = Image("00000:""00000:""00000:""00000:""09390:")
        boat15 = Image("00000:""00000:""00000:""00000:""00000:")
        boat16 = Image("00000:""00000:""00000:""00000:""09390:")
        boat17 = Image("00000:""00000:""00000:""93039:""09390:")
        boat18 = Image("00000:""00000:""90909:""93039:""09390:")
        boat19 = Image("00000:""93039:""90909:""93039:""09390:")
        #boat20 = Image("00000:""90000:""00000:""00000:""00000:")
        all_boat =[boat1, boat2, boat3, boat4, boat5,  boat7, boat8,
        boat9, boat10,boat11, boat12, boat13,
        boat14, boat15, boat16, boat17, boat18, boat19]
        display.show(all_boat, loop=True, delay=100)
    else:
        display.set_pixel(0,0,0)
    if pin1.is_touched():
        display.set_pixel(4,0,9)
        display.show("59102105139")#, loop=True, delay=100)

    else:
        display.set_pixel(4,0,0)
    sleep(10)

    if pin2.is_touched():
        display.set_pixel(4,0,9)
        display.show(Image.DUCK)#, loop=True, delay=100)
        #count = button_b.was_pressed("stop")
    else:
        display.set_pixel(4,0,0)
    sleep(10)



