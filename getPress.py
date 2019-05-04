from microbit import *
while True:
    sleep(3000)
    count = button_a.get_presses() #การรับค่าว่ามีเท่าไร
    display.scroll(str(count))



    #เริ่ม
    #if button_a.is_pressed(): ตัวกด is_gesture
    #    display.scroll("TONG") แสดงข้อมูลออก
    #if button_b.was_pressed():
    #    display.show(Image.ANGRY) หยุด


